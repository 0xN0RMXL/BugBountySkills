# SKILL: GraphQL Introspection Attacks
## Version: 1.0 | Domain: api

---

(See WEB/graphql_attacks.md for full coverage — this is the introspection-specific deep dive)

## INTROSPECTION QUERY (full)
```graphql
query IntrospectionQuery {
  __schema {
    queryType { name }
    mutationType { name }
    subscriptionType { name }
    types {
      kind name description
      fields(includeDeprecated: true) {
        name description
        args { name description type { ...TypeRef } defaultValue }
        type { ...TypeRef }
        isDeprecated deprecationReason
      }
      inputFields { name description type { ...TypeRef } defaultValue }
      interfaces { ...TypeRef }
      enumValues(includeDeprecated: true) { name description isDeprecated deprecationReason }
      possibleTypes { ...TypeRef }
    }
    directives { name description locations args { name description type { ...TypeRef } defaultValue } }
  }
}
fragment TypeRef on __Type { kind name ofType { kind name ofType { kind name ofType { kind name ofType { kind name ofType { kind name ofType { kind name ofType { kind name } } } } } } } }
```

## WHEN INTROSPECTION IS DISABLED
- **clairvoyance** — wordlist-based schema recovery via suggestion-based fuzzing.
- **graphql-path-enum** — build schema from error messages.
- Check for GraphQL IDE endpoints: `/graphiql`, `/playground`, `/explorer`, `/altair`.

## POST-INTROSPECTION
1. List all queries, mutations, subscriptions.
2. Identify sensitive fields (password, token, ssn, creditCard).
3. Test each with low-priv user for BOLA/BFLA.
4. Test mutations for mass assignment.

## TOOLS
inql (Burp), graphql-cop, graphql-voyager (visual schema), clairvoyance.

## REFERENCES
Doyensec GraphQL testing
