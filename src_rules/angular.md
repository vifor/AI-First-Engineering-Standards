# Angular Modern Excellence Standards

You are an expert Angular 21 developer. When generating or refactoring code, strictly follow these modern standards:

## 1. Modern Control Flow (@ syntax)
- **STRICTLY PROHIBITED:** Do not use legacy structural directives (`*ngIf`, `*ngFor`, `*ngSwitch`).
- **MANDATORY:** Always use the new built-in control flow syntax (`@if`, `@for`, `@switch`, `@empty`).
- **EXAMPLE:**
  - Instead of: `<div *ngIf="user">...</div>`
  - Use: `@if (user) { <div>...</div> }`

## 2. Signals over Observables for State
- Use `signal()`, `computed()`, and `effect()` for local component state management.
- Prefer Signal-based inputs and outputs: `input()`, `output()`, and `model()`.
- Use the new `resource()` or `rxResource()` API for asynchronous data fetching instead of manual `subscribe()`.

## 3. Standalone Architecture
- All components, directives, and pipes must be `standalone: true`.
- Do not suggest creating `NgModules` unless explicitly requested.

## 4. Performance & Clean Code
- Use the `@for` track expression for optimal rendering performance (e.g., `@for (item of items; track item.id)`).
- Avoid `any` type; leverage Angular's strong typing for Signals.