# Lab: Welcome to React, Next.js & TailwindCSS

## Overview

React is great! And though it does A LOT, it's not a full framework. In other words, many common tasks are not handled out of the box by React. So it's up to us devs to make some decisions about how to use React in combination with other tools.

One great "stack" is to use Next.js (which builds on top of React) and style with Tailwind.

Your job is to create a `Cookie Stand Admin` app using [Next.js](https://nextjs.org/){:target="_blank"} and style using [Tailwind CSS](https://tailwindcss.com/){:target="_blank"}.

## Feature Tasks and Requirements

- The `spec` for lab is screen shot of [Cookie Stand Admin Version 1](./cookie-stand-admin-version-1.png){:target="_blank"}
- `pages/Index.js` should...
  - Have `<Head>` component with page title set to `Cookie Stand Admin`
  - Have a `header` component that matches spec.
  - Have a `<main>` component containing `<form>` and a placeholder component showing JSON string of last created Cookie Stand.
  - Have a `<footer>` component that matches spec.
- Style app using TailwindCSS utility classes.

## Implementation Notes

- > npx create-next-app --example with-tailwindcss cookie-stand-admin
- strip out unused files
  - Won't break if they get left in, but a good practice to remove stuff you're not using.
- Pro tip: [Tailwind CSS Extension Pack](https://marketplace.visualstudio.com/items?itemName=andrewmcodes.tailwindcss-extension-pack){:target="_blank"}

### User Acceptance Tests

No testing required.

## Configuration

Create `cookie-stand-admin` repository in Github

Use the folder created by `create-next-app` as the root of your project's git repository.

Refer to [Lab Submission Instructions](../../../reference/submission-instructions/labs/){:target="_blank"} for detailed instructions.

### Stretch Goals

- Refactor to move components to own functions.
- Refactor to move components to own files.
- Add more styling
- Link to another page within the app
