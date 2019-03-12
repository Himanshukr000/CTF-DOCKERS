/* eslint-disable no-console */
import sanitizeHtml from 'sanitize-html';
import sha1 from 'node-sha1';

module.exports = (app) => {
    app.get('/sanitize', (req, res, next) => {
        const content = sanitizeHtml(req.query.content, {
            allowedTags: ['b', 'i', 'strong', 'br', 'pre']
        });
        res.status(200).send({
            content: content,
            checksum: sha1('zZSfx7rlDZxdUvANh12MzYAaiT9XHkiV' + content)
        });
    });
};
  