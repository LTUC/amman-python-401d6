# Cookie Stand Demo

## Modify API

- Three small changes are needed to API.
- By default, minimal information is included in the JWT returned by API.
- We need to make a small change to include more info bundled in the tokens.
- `project/views.py`

```python
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["email"] = user.email
        token["username"] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

```

- The second change is to modify `project/urls.py` to look like this...

```python
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views
from .views import MyTokenObtainPairView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/cookie-stands/", include("cookie_stands.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path(
        "api/token/",
        MyTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "api/token/refresh",
        jwt_views.TokenRefreshView.as_view(),
        name="token_refresh",
    ),
]
```

- Now email and username are included in the tokens returned after logging in.
- NOTE: It is NOT a requirement of an API to return such  info. Each API will differ. The point is to know you can.
- The third change is to `project/settings.py` to configure how long the access token last before expiring. Add this line to settings, usually at the bottom.

```python
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(
        seconds=60 * 60
    ),  # lasts for 60 minutes
}
```

## Create App

- `npx create-next-app --example with-tailwindcss cookie-stand-demo`

## Install Dependencies

- `npm i axios swr jsonwebtoken`
- Alternately, install each one when needed

## Skeleton Home Page

- Replace `index.js` placeholder content with...

```javascript
import Head from 'next/head'

export default function Home() {

    const user = null;

    return (
        <div>
            <Head>
                <title>Cookie Stand Demo</title>
                <link rel="icon" href="/favicon.ico" />
            </Head>

            <main className="p-4 space-y-8 text-center">
                <h1 className="text-4xl">Fetching Data from Authenticated API</h1>
                <button className="p-2 text-white bg-gray-500 rounded">Login</button>
                {user ? (
                    <h2>Welcome {user.username}</h2>
                ) : (
                    <h2>Need to log in</h2>
                )}
            </main>
        </div>
    )
}
```

- Page should render `Need to log in`
- Change `user = null` to `user = {username:'somebody'}` and see what happens

```javascript
const user = { username: 'somebody' };
```

- `Welcome somebody` should render.
- The task now is to offload responsibility of providing the user to some other service.
- Introducing `auth.js`
  - copy over `contexts/auth.js` from solution
  - copy over `.env.local` from solution's `sample.env.local`
- There's less than 50 lines of code there, but the do alot.
- But before looking under the hood let's just see how to use it.
- `auth.js` defines a `context` which does two things - enables providing shared "stuff" and enables consuming shared "stuff." That's pretty vague, so let's go through the steps.
- Modify `pages/_app.js`

```javascript
import 'tailwindcss/tailwind.css'
import { AuthProvider } from '../contexts/auth'

function MyApp({ Component, pageProps }) {
    return <AuthProvider>
        <Component {...pageProps} />
    </AuthProvider>
}

export default MyApp
```

- `_app.js` contains the parent for all page components.
- By wrapping `AuthProvider` around then all page components, and all their children, have access to auth provided "stuff" - as long as these components ask the right way.
- `pages/index.js`
  - Add `import { useAuth } from '../contexts/auth'`
  - Change `user` definition line to `const { user } = useAuth();`
- Should still render `Need to log in`
- To change that we need to log in of course.
- `pages/index.js`
  - Modify user definition line to be `const { user, login } = useAuth();`
  - Add onClick handler to login button.
    - `<button onClick={() => login('somebody', 'somepassword')}`
    - NOTE: the username and password must match known user in API's database
- Page should still render `Welcome somebody` but this user is real!
- Logging out is just as easy
- Modify `pages/index.js` to  handle logging out

```javascript
import Head from 'next/head'
import { useAuth } from '../contexts/auth'

export default function Home() {

    const { user, login, logout } = useAuth();

    return (
        <div>
            <Head>
                <title>Cookie Stand Demo</title>
                <link rel="icon" href="/favicon.ico" />
            </Head>

            <main className="p-4 space-y-8 text-center">
                <h1 className="text-4xl">Fetching Data from Authenticated API</h1>
                {user ? (
                    <>
                        <h2>Welcome {user.username}</h2>
                        <button onClick={logout} className="p-2 text-white bg-gray-500 rounded">Logout</button>
                    </>
                ) : (
                    <>
                        <h2>Need to log in</h2>
                        <button onClick={() => login('rudy', 'rudy')} className="p-2 text-white bg-gray-500 rounded">Login</button>
                    </>
                )}
            </main>
        </div>
    )
}
```

- And that's Auth in action.
  - Dig as deep as you care to into `auth.js` file and/or django project changes.
  - But stress to students that they should be increasingly comfortable using a library's public features and only digging into implementation details when they've got the time and the curiousity.

## Resources

- The only reason we bothered to log in was to get access to the API's resources.
- REMINDER: A `resource` in a restful API can be considered the `noun` your API manages.
  - E.g. for `GET /api/v1/shoes` the resource is `shoes`
- We've been working with Cookie Stands, that's the `resource` we want to perform CRUD operations on.
- There are plenty of ways interact with an API from the front end, some of which folks learned in 301.
- We're going to work with a couple newer tools that are getting really popular.
- These tools are going to be used within a `custom hook` named `useResource`
  - Copy over `hooks/useResource.js`
  - Update `pages/index.js` to render a `StandList` component.

```javascript
import Head from 'next/head'
import { useAuth } from '../contexts/auth'
import useResource from '../hooks/useResource'

export default function Home() {

    const { user, login, logout } = useAuth();
    const { resources, loading } = useResource();

    return (
        <div>
            <Head>
                <title>Cookie Stand Demo</title>
                <link rel="icon" href="/favicon.ico" />
            </Head>

            <main className="p-4 space-y-8 text-center">
                <h1 className="text-4xl">Fetching Data from Authenticated API</h1>
                {user ? (
                    <>
                        <h2>Welcome {user.username}</h2>

                        <button onClick={logout} className="p-2 text-white bg-gray-500 rounded">Logout</button>

                        <StandList stands={resources} loading={loading} />

                    </>
                ) : (
                    <>
                        <h2>Need to log in</h2>
                        <button onClick={() => login('rudy', 'rudy')} className="p-2 text-white bg-gray-500 rounded">Login</button>
                    </>
                )}
            </main>
        </div>
    )
}

function StandList({ stands, loading }) {

    if (loading) return <p>Loading...</p>

    return <ul>
        {stands.map(stand => (
            <li key={stand.id}>{stand.location}</li>
        ))}
    </ul>
}
```

- But we can get more from `useResource`, we can do CRUD! Well, not Update, that's left for students to do.
- Let's add ability to create a resource, in this case a cookie stand.
- Define `createResource` const alongside `resources` from return value of `useResource` hook.
- Render a `<StandCreateForm >`
- Define a `<StandCreateForm>`

```javascript
import Head from 'next/head'
import { useAuth } from '../contexts/auth'
import useResource from '../hooks/useResource'

export default function Home() {

    const { user, login, logout } = useAuth();
    const { resources, loading, createResource } = useResource();

    return (
        <div>
            <Head>
                <title>Cookie Stand Demo</title>
                <link rel="icon" href="/favicon.ico" />
            </Head>

            <main className="p-4 space-y-8 text-center">
                <h1 className="text-4xl">Fetching Data from Authenticated API</h1>
                {user ? (
                    <>
                        <h2>Welcome {user.username}</h2>

                        <button onClick={logout} className="p-2 text-white bg-gray-500 rounded">Logout</button>

                        <StandCreateForm onCreate={createResource} />

                        <StandList stands={resources} loading={loading} />

                    </>
                ) : (
                    <>
                        <h2>Need to log in</h2>
                        <button onClick={() => login('rudy', 'rudy')} className="p-2 text-white bg-gray-500 rounded">Login</button>
                    </>
                )}
            </main>
        </div>
    )
}

function StandList({ stands, loading }) {

    if (loading) return <p>Loading...</p>

    return <ul>
        {stands?.map(stand => (
            <li key={stand.id}>{stand.location}</li>
        ))}
    </ul>
}

function StandCreateForm({ onCreate }) {

    function handleSubmit(event) {
        event.preventDefault();
        const standInfo = {
            location: event.target.location.value,
            minimum_customers_per_hour: parseInt(event.target.min.value),
            maximum_customers_per_hour: parseInt(event.target.max.value),
            average_cookies_per_sale: parseFloat(event.target.avg.value),
        }
        onCreate(standInfo);
        event.target.reset();
    }
    return (
        <form className="space-x-4" onSubmit={handleSubmit}>
            <input className="border-2 border-black" name="location" placeholder="location" />
            <input className="border-2 border-black" name="min" placeholder="min" />
            <input className="border-2 border-black" name="max" placeholder="max" />
            <input className="border-2 border-black" name="avg" placeholder="average" />
            <button className="p-2 text-white bg-gray-500 rounded">CREATE</button>
        </form>
    )
}
```

- So now we can Read and Create resources. Let's move on to Delete.
- **NOTE:** Get the students to lead the way here
- First we need to define `deleteResource`
  - `const { resources, loading, createResource } = useResource();`
- Next, modify `<StandList>` declaration
  - `<StandList stands={resources} loading={loading} onDelete={deleteResource} />`
- Last, update `<StandList>` component definition to  allow deletes...

```javascript
function StandList({ stands, loading, onDelete }) {

    if (loading) return <p>Loading...</p>

    return <ul>
        {stands?.map(stand => (
            <li key={stand.id} className="space-x-2">
                <span>{stand.location}</span>
                <span onClick={() => onDelete(stand.id)}>[X]</span>
            </li>
        ))}
    </ul>
}
```

## Summary

There you have it, 3/4 of CRUD!

The job in lab is to modify your front end client and back end to enable authenticated clients to perform restful operations on your API.
