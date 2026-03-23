# AWS Lambda, DynamoDB & SAM Standards

You are an expert AWS serverless developer. When generating or refactoring infrastructure and Lambda code, strictly follow these standards:

## 1. Add CORS Headers to Every Lambda Response Path

- **STRICTLY PROHIBITED:** Do not add CORS headers only to the success response.
- **MANDATORY:** Include `Access-Control-Allow-Origin` (and other required CORS headers) in **every** response object — success, validation error, caught exception, and any early return.
- **Why:** A Lambda that returns a 400 or 500 without CORS headers will cause the browser to report a CORS error instead of the actual error, making debugging extremely difficult.
- **EXAMPLE:**
  ```ts
  const CORS_HEADERS = {
    'Access-Control-Allow-Origin': '*',
    'Content-Type': 'application/json',
  };

  // Every return must include CORS_HEADERS
  if (!body.email) {
    return { statusCode: 400, headers: CORS_HEADERS, body: JSON.stringify({ error: 'email required' }) };
  }
  return { statusCode: 200, headers: CORS_HEADERS, body: JSON.stringify({ success: true }) };
  ```

## 2. DynamoDB TTL Must Be a Number (Unix Epoch), Not a String

- **STRICTLY PROHIBITED:** Do not set TTL attributes as ISO date strings or any non-numeric type.
- **MANDATORY:** TTL values must be a `Number` representing Unix epoch in **seconds**.
- **Why:** DynamoDB's TTL mechanism only recognizes numeric epoch values. A string attribute will be silently ignored — items will never expire.
- **EXAMPLE:**
  ```ts
  // WRONG
  ttl: new Date(Date.now() + 86400000).toISOString()

  // CORRECT
  ttl: Math.floor((Date.now() + 86400000) / 1000)
  ```

## 3. DynamoDB TTL in SAM Template: Use TimeToLiveSpecification, Not AttributeDefinitions

- **STRICTLY PROHIBITED:** Do not add the TTL attribute to `AttributeDefinitions` in a DynamoDB SAM/CloudFormation resource.
- **MANDATORY:** Enable TTL exclusively via `TimeToLiveSpecification`.
- **Why:** `AttributeDefinitions` is only for key attributes (partition key and sort key). Adding a TTL attribute there causes a CloudFormation deployment error.
- **EXAMPLE:**
  ```yaml
  # WRONG
  AttributeDefinitions:
    - AttributeName: pk
      AttributeType: S
    - AttributeName: ttl       # <-- WRONG, causes deployment failure
      AttributeType: N

  # CORRECT
  AttributeDefinitions:
    - AttributeName: pk
      AttributeType: S
  TimeToLiveSpecification:
    AttributeName: ttl
    Enabled: true
  ```
