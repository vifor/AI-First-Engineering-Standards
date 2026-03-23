# React & Next.js Standards

You are an expert React and Next.js developer. When generating or refactoring code, strictly follow these standards:

## 1. Never Access Browser APIs Outside of useEffect

- **STRICTLY PROHIBITED:** Do not read `localStorage`, `sessionStorage`, `window`, or `document` during render or in component body initialization.
- **MANDATORY:** Access browser APIs only inside `useEffect` or event handlers.
- **Why:** Next.js renders components on the server first. Browser APIs do not exist on the server. Accessing them during render causes a hydration mismatch error that silently breaks the UI.
- **EXAMPLE:**
  ```tsx
  // WRONG — causes hydration error
  const [value, setValue] = useState(localStorage.getItem('key'));

  // CORRECT
  const [value, setValue] = useState<string | null>(null);
  useEffect(() => {
    setValue(localStorage.getItem('key'));
  }, []);
  ```

## 2. Wrap Exposed Hook Functions in useCallback

- **MANDATORY:** Any function exposed by a custom hook that will be used in a `useEffect` dependency array must be wrapped in `useCallback`.
- **Why:** Functions defined inside hooks are recreated on every render. If a component puts that function in a `useEffect` dependency array, the effect re-runs on every render, causing infinite loops, duplicate API calls, or duplicate rendered items.
- **EXAMPLE:**
  ```ts
  // WRONG — loadMore is a new reference on every render
  const loadMore = () => { fetchData(cursor); };

  // CORRECT
  const loadMore = useCallback(() => { fetchData(cursorRef.current); }, []);
  ```

## 3. Exclude Backend Code from Next.js tsconfig

- **MANDATORY:** When a Next.js project coexists with backend code (e.g., AWS Lambda functions) in the same repository, add the backend folder to the `exclude` array in `tsconfig.json`.
- **Why:** Next.js uses `tsconfig.json` to determine what to compile. Without exclusion, `next build` will attempt to compile Lambda TypeScript files and fail with unexpected type or module errors.
- **EXAMPLE:**
  ```json
  {
    "exclude": ["node_modules", "backend"]
  }
  ```
