# Checklist: SSTI
- [ ] Probe `${7*7}`, `{{7*7}}`, `<%= 7*7 %>`, `#{7*7}`, `*{7*7}`
- [ ] Identify engine via probes / response body / framework
- [ ] Achieve RCE via gadget chain (engine-specific)
- [ ] Read environment / files
- [ ] Bypass sandbox (older Twig, Jinja2 with __mro__ traversal, Velocity)
- [ ] Test in: email body customization, error message templates, name field, admin notifications
- [ ] Test in PDF/HTML report generators
- [ ] Test in Marketing email templates
