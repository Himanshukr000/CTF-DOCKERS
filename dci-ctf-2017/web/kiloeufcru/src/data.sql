CREATE TABLE facts (id int, text string);
CREATE TABLE apikeys (id int, text string, demo int);
CREATE TABLE strangely_long_name_for_a_table (strangely_long_name_for_a_column text, i1 int, i2 int);

INSERT INTO apikeys VALUES (0, 'alkfdnasldkfnal3wfnalkfnalfn3alkfn3alkf', 1);

INSERT INTO strangely_long_name_for_a_table VALUES ('DCI{the_best_filter_the_best_signature_the_best_app}', 0, 0);

INSERT INTO facts VALUES (0, 'Odontophobia is the fear of teeth.'),
(1, 'Cats sleep 16 to 18 hours per day.'),
(2, 'Karoke means "empty orchestra" in Japanese.'),
(3, 'When you die your hair still grows for a couple of months.'),
(4, 'The pancreas produces Insulin.'),
(5, "Elephants are the only mammals that can't jump.");
