# SunshineCTF 2017 Challenges

This repo is to be used by challenge authors to host the sources of SunshineCTF 2017 challenges.

## Directory Structure

* Challenge category (e.g. `Web`, `Crypto`, `Pwn`)
   * Points-Challenge (e.g. `100-MyEasyChallenge`, `500-ThisIsLiterallyImpossible`)
     * The challenge itself

## Required Files

| File name         | Description
|-------------------|-------------
| `description.md`  | Markdown formatted description as should be displayed to players on the challenge description page.
| `README.md`       | Detailed information including a description of how the challenge works, steps to build and deploy this challenge, how to maintain it, and the intended solution. This will not be given to players.
| `flag.txt`        | The challenge's flag in the format `sun{flag_goes_here}`. If the flag is of a format different than this, please mention this explicitly in your `README.md` file.

If a challenge has files that should be downloadable from the challenge description, create a subdirectory `attachments` and place the files there.

An example challenge is available in `Stego/100-Hello-Friend`.
