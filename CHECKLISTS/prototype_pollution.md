# Checklist: Prototype Pollution
- [ ] Probe `__proto__[admin]=true` in query string
- [ ] Probe `{"__proto__":{"admin":true}}` in JSON body
- [ ] Probe `constructor[prototype][admin]=true`
- [ ] Confirm pollution via `{}.admin` in browser console (client-side) or via gadget detection (server-side)
- [ ] Find gadget — look for `merge`, `extend`, `assign`, `set`, `defaultsDeep`, `cloneDeep` calls
- [ ] Client gadgets: jQuery $.get, AngularJS, Lodash _.template, React dangerouslySetInnerHTML
- [ ] Server gadgets: Express render options, child_process spawn, lodash template, hbs render
- [ ] Test ppfuzz / ppmap against the app
