# Triage Rules

1. **Critical severity**: classify as critical when the report explicitly indicates data loss, confirmed security compromise, complete service outage, or a safety-critical failure.
2. **High severity**: classify as high when a major production function is unusable for affected users, a severe regression blocks an important workflow, or the issue has substantial operational impact without meeting a critical rule.
3. **Medium severity**: classify as medium when a feature is impaired but a reasonable workaround exists, or the issue materially affects a subset of users.
4. **Low severity**: classify as low when the issue is cosmetic, wording-only, minor usability friction, or otherwise has negligible functional impact.
5. **Priority**: critical severity maps to P0; high maps to P1; medium maps to P2; low maps to P3.
6. **Security signal**: explicit authentication bypass, credential exposure, unauthorized access, or confirmed security compromise raises severity to at least high; confirmed compromise is critical.
7. **Evidence discipline**: missing evidence never becomes a fabricated fact. Missing reproduction steps, expected behavior, actual behavior, environment, or logs are reported as missing information when applicable.
8. **Conflict handling**: when multiple severity signals are present, the highest applicable severity rule wins and all triggered rules are listed.
