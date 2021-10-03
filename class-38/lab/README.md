# Lab: Cookie Stand Admin Version 2

## Overview

Your job is to continue work on `Cookie Stand Admin` app using [Next.js](https://nextjs.org/){:target="_blank"} and style using [Tailwind CSS](https://tailwindcss.com/){:target="_blank"}.

## Feature Tasks and Requirements

- The `specs` for lab are screen shots [Cookie Stand Admin Version 2](./cookie-stand-admin-version-2.png){:target="_blank"} and [Cookie Stand Admin No Stands](./cookie-stand-admin-no-stands.png){:target="_blank"}
- `pages/Index.js` should return top level component `<CookieStandAdmin>`
- `<CookieStandAdmin>` details...
  - Have a `<Head>` component.
  - Have a custom `<Header>` component that matches spec.
  - Have a `<main>` component.
  - Within `<main>` have custom `<CreateForm>` and `<ReportTable>` components.
  - Have a custom `<Footer>` component that matches spec.
  - Import time slot data from supplied `data.js` file.
- `<Head>` should set page title `Cookie Stand Admin`
- `<Header>` component should have Next `<Link>` to `overview` page.
- `<CreateForm>` component details...
  - Receive an `onCreate` function to be called when form is submitted.
  - `onCreate` should be passed argument object representing new cookie stand.
    - Object should have `location` property.
    - Object should have `hourly_sales` property with hard coded `[48, 42, 30, 24, 42, 24, 36, 42, 42, 48, 36, 42, 24, 36]`
- `<ReportTable>` details...
  - should receive `hours` on props that is an array cookie stand hours of operation.
  - should receive `reports` on props that is an array all cookie stand objects.
  - If `reports` is empty then render `<h2>No Cookie Stands Available</h2>`
  - If `reports` is not empty then render a `table` with `thead`,`tbody` and `tfoot` components.
  - Component should render to match spec.
  - Component is responsible for tallying totals for each cookie stand as well as all cookie stands per hourly slot.
- `<Footer>` component details...
  - Should receive `reports` array on props.
  - Should display `X Locations World Wide` where `X` is number of cookie stands.
- `<Header>`,`<Footer>`,`<CreateForm>` and `<ReportTable>` should each be in own file inside top level `components` folder.
- Those components should be imported into `Index.js`
- `Overview` page details...
- should live in `pages/overview.js`
- should render `<Link href="/"><a>Return to Main page</a></Link>`
- Style all components using TailwindCSS utility classes to match spec.

## Implementation Notes

- Continue work in `cookie-stand-admin` repository
- **IMPORTANT** Complete version 1 tasks before moving to version 2 features.
- Pro tip: [Tailwind CSS Extension Pack](https://marketplace.visualstudio.com/items?itemName=andrewmcodes.tailwindcss-extension-pack){:target="_blank"}

### User Acceptance Tests

No testing required.

## Configuration

Continue work in `cookie-stand-admin` repository in Github

Refer to [Lab Submission Instructions](../../../reference/submission-instructions/labs/){:target="_blank"} for detailed instructions.

### Stretch Goals

- Flesh out `Overview` page to do more
- Remove hard coding from `<CreateForm>` and properly calculate hourly sales per cookie stand.
- Add delete icons.
  - Pro Tip: [Heroicons](https://heroicons.com/){:target="_blank"}
- Really stretch out and make delete icons functional.
- Persist Cookie Stand data.
