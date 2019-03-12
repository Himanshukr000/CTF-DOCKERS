# Colonel Mustard's Simple Site

We know Colonel Mustard is up to something--can you find a way in to tell us what?

This challenge was a basic SQL Injection challenge. The query used in the database was `SELECT 1 FROM users WHERE user='$username' AND password='$password'`
Some sample injections that would have worked (in the form username/password):
- 1/' OR '1'='1
- ' OR '1'='1'--/'--
