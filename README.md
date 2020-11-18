# What is Flask-Secrets? ![CI](https://github.com/nickjj/flask-secrets/workflows/CI/badge.svg?branch=master)

It's a Flask extension that makes it easy to generate secure secret keys and
tokens.

After installing it you'll be able to run `flask secrets` to generate a number
of tokens that you can use for your `SECRET_KEY`, database passwords, API keys,
auth tokens or whatever else you need secret tokens for.

## Table of contents

- [Installation](#installation)
- [Ensuring the `secrets` command is available](#ensuring-the-secrets-command-is-available)
- [Going over the `secrets` command](#going-over-the-secrets-command)
- [FAQ](#faq)
  - [Why are the tokens prefixed with dev, test and prod?](#why-are-the-tokens-prefixed-with-dev-test-and-prod)
  - [Why did you generate 10 tokens for each prefix?](#why-did-you-generate-10-tokens-for-each-prefix)
  - [Why did you pick 99 characters as a length?](#why-did-you-pick-99-characters-as-a-length)
  - [Why did you limit tokens to letters and digits?](#why-did-you-limit-tokens-to-letters-and-digits)
- [About the Author](#about-the-author)

## Installation

`pip3 install Flask-Secrets`

That's it!

There's no need to even initialize anything in your Flask app because it's just
a CLI command that gets added to your Flask app.

*But if you're curious, a complete example Flask app can be found in the
[tests/
directory](https://github.com/nickjj/flask-secrets/tree/master/tests/example_app).*

#### Requirements:

- Python 3.6+
- Flask 1.0+

## Ensuring the `secrets` command is available

You'll want to make sure to at least set the `FLASK_APP` environment variable:

```sh
# Replace `hello.app` with your app's name.
export FLASK_APP=hello.app
export FLASK_ENV=development
```

Then run the `flask` binary to see its help menu:

```sh

Usage: flask [OPTIONS] COMMAND [ARGS]...

  ...

Commands:
  secrets  Generate a set of random secret tokens.
```

If all went as planned you should see the new `secrets` command added to your
list of commands.

## Going over the `secrets` command

Running `flask secrets --help` will produce this help menu:

```sh
Usage: flask secrets [OPTIONS]

  Generate a set of random secret tokens.

  They are suitable for your SECRET_KEY, passwords, API keys and more.

Options:
  --length INTEGER  Character length.  [default: 99]
  --count INTEGER   Generate N tokens.  [default: 10]
  --prefix TEXT     1 or more key prefixes.  [default: dev_, test_, prod_]
  --help            Show this message and exit.

```

And if you run `flask secrets`, you'll end up with something like this by
default:

```sh
dev_zQ0xyfjkundFVF9GiR0PnT8DbTVczXd3yumese3RGlKax6OIOBWku4giwUL45LKIPhnCaxSfNNyuMUU5CgZnrplmlaHBvQAAFx0
dev_CDJ7VtrzXn7n87bw3nJORaSAUHeRTW7Y66habnI5araUlDNBj1XZJhEVUZoQbnmC1DyFrVWEb7o3gTHl6yd8brqe7frJtqu0PDR
dev_568Fu6SX4JsvtY1IoIpH9ZDzx2TO6kaNcRBCDJ4s4dmAK6cODcs33qawHTDeW8ENXYT5YI0Q8upRT2oSBjEoyX8tENyPu89awSd
dev_Y6vZbxzy86bn5fX2fmXMcPgtL02zBXAeuAQfUdLJ64yycZWTOoVBr0qJRyYvz0T1D5XTKOpon6ngVGhDmOsdOjhtNDF89ftJgOy
dev_1dQ5K3YE2ORh1XJuR1pzPuagiB1fhGIvDNzIe5rBi8SiRoN0IYkKz8lSqUUwi1I6Xe7mWG6Z2938NgfnlYjeMQUFe18CFI5rh4l
dev_Tj5EknS2VPXcqSHAHm0NPZzDhMspcE0VMyo6I6SHGdXpUqMysryl3iPPMaoFrR2OmccEpvq5zSv6BGMf5KPBH8hEYlUKcpA8Jfm
dev_wNnDkOeMUlE0mFu7UPi5b2pkizns5bLhtrqCcdmEXks7sDbIsmgVGaph6eO6zXyUd5YwjFec4JVFB0bRxphZ5PB4t1OKCic5QR5
dev_UNAXyQodUA2kiQlAwUKxvLxGd9MmsDOplwAq2omP3R7z5ibEd1ICXR5tA2mBdIoe4jrK6c2pbL0ERuoVjXqTOqYtIDZY9p71PGh
dev_WQcLSeXc4h9iZqb7SV0CUH9vWNmwg3quJGflxZ9qzMqoq1nKMa1N091rzVBCqbAsykF2v0SmhRKpPHrZ1xIjV9rrDaRuFVKH0Nj
dev_Sr8rN495pBnE6IBwiSYefQWfNX87mTvBmiHzBpTTJVNeTZSs6xZEjByH5zlp7BOrykvmNqscA6Iat4VOyOR9pRdrNmcah20V3YB
test_UyPdaxcL836BTzqHYZ3sLkQj6bzJUsmMqENP4sMoTpc7QarsluSBTmgjTdCy3zvocrNafXPliMAwENgiORwzb5pBWsrBNNXUiJi
test_6PwVF9TlUybXpWuraV9qPP9RESHiDrqY7AMVrPuI2hFLs68ePf9VoazBHlrLtX1uOeDEQN0rPPUP2H06hkSG8RWOF3DiOGyhmda
test_zdVPbucsNsJC5Ay8bf9AkByeyKPcKhmWnbXSdu84derV4RWjk2n2I2ouY3C1ta7xWp6uRnFIgDT56vYFozhpfVwbXHhkHskulVi
test_JDesFe6K7MHhQY2g9CwdWBm44ZEQ3hWFTCxcZ37KnLP4eajVj1ol616G3ZkIdr7ST3m71g5UFhXEurVexle7rWfNnDCId4EWsw1
test_p4MJpL8uG15dge6jfMqLbW339s7i9Uk2mU12mDbtHqWM14SEqn1YlYbqfDStVaMXFZ9Bsnlv5OeoveTq8ERNz1WZSm4vYJbhKkV
test_5AAsQEyu8ffekPzqhYFU2yJ97AHhnoIO30TkYZ9NfI7N9tUA68TiXj8xj5pka0Wu9YffnMgfhfkukVPS9LqE5JYhnsG8LzN2IzJ
test_ymQxojdxDCvOxokGE6Y2w6LkZQwwJIRiL59SjBQuSZ4rDr7aTF42s2IcCOIqbOvlO1eskaPFSyDdvw57XmX7oRe4Bh4sgptdDHx
test_b5SY9YG7r0j6UI8SvJDOycI6uoXNfnbrO5aA3wqHopDhtCsSPhoLnFoQVJWJevMfEIKpTr0TDlo3A1166FN88wH51RD3PgAMdJ1
test_8R9AydIXx3gju5QCwH9E0ex9lJJ8r92bUDGdzbymkruQ1VlqBJlCJvxd5BCIUfEec1DxT0FMoeYqaGGs2IZLZsmrnh6CraiaCtk
test_bMQuKfxX7Zmr3nCvQIHUyLNjroyQab9B3x0ZDS7A99OVpfzqJMkhxxVvWQ8TtBAYgUZhVkGNlHDhQwlrIWiBAgDBLZhAW6nRNcw
prod_rqld1qJJJyfT7zYpMN2G9t1AkcoR9IIQzzapNSBzpFsw3EjYnMManHe7v98i202kzTO9RdEIRjIGQH0Qc5qVzPfnkmITob1XJuT
prod_JEH0geowxZBCoYPURzAasexTJkQXqPK7qG8VmFGxEcyA0NkcG4NnBjKqWMgMmElOIP5TN3UuNjLg3gzvM3pFj1ckhD5Qpyg1ztY
prod_tobmUu7IaYo2Qgq9LXEGIpaVa1jxWlJqlHDoMhWHsdkxwESL6F5eG5KJDKLwVEnS3nzRl8BOhmPLhet4c600Fm69U7F6A6jpVHV
prod_H4vBS42lNobZ8jnoPX0QvVsDAzSvCWnPPdmbiWOueSwmMSknv485Eq38OjMNSmNdOcFzlRFplXNo3TXWCuDmVCvWsdcVfPsdtGj
prod_q3jPJ9rCiuNEx8Uyz2jW16zQ5SqYaehitUnQoGe74CMJAN4btF73jzyrgGAiSqGBL949kuNt3Yl9GcVY9SixC9mCLfP52sQoadt
prod_mWDTYYW4b8TGQ1DfUFYW1SLKI3YLzPzPzThqUlVKWaOU9G7tYSybar4ZPIMsDNtqTih6S6vULRxsZU5xMk1lriGy6roje2fZ006
prod_eGXFj5bJLPNmvHorgv7m9r0YNxhOy1tKG2A0WUT5jWYUj7YS9MPW2mHRJulNMIh7qTdvQMZGFtfC5ueuP4aFmOWQTBy744m5JLw
prod_hx94QSlPiR5pD3DX0YJJlANBbOm0Xjg6fc0Pbhn27PpYYVxzc9hkGLgquDl87gm0cltZGfKXdvaeRevfEaxIOytzFEZR1tfwXZ2
prod_Vlgc1gK9mOjrd8xUaNPRzyA3e0owdedViWhYd3wj0iEfgdjZRoFFjkVhV3tA9YhsA49k0hMDz8dTYDGqPXN5zRfR9Ruzoe6zoOo
prod_i1c8G6QdaxjHwGMmj6myc2Tvd1MpUoPSfDXpeb26QfIDitiW9R41Jf8sNFBlrpQE4ugEdhtM6pjiCzDx7MAoyKKeTdhlk2Z54X8

```

There's 1 token on each line and they're generated with uppercase / lowercase
letters and digits.

#### 30 random tokens

By default you'll get 10 tokens for each environment you might run your app in.
Each token can be used individually however you see fit across any environment.
They are not associated to each other in any way shape or form.

## FAQ

### Why are the tokens prefixed with dev, test and prod?

This is a convention I took from Stripe. I really like how Stripe's keys
include prefixes like `pk_test_`, `sk_test_`, `pk_live_` and `sk_live_`. At a
glance you can tell what type of key it's for and what environment it's
associated to.

By default this tool prefixes each environment you might run your app in. You
can always customize the prefixes by passing in 1 or more prefix flags, such as
`--prefix apples_ --prefix oranges_`. You can also do `--prefix ""` to omit any
type of prefix.

### Why did you generate 10 tokens for each prefix?

Most real world applications will require having at least a `SECRET_KEY`, 
PostgreSQL password and maybe a Redis password.

That puts us at needing at least 3 tokens. If you happen to be doing client
work you might find yourself creating additional passwords for various services
too. It adds up!

If this tool only generated 1 token at a time then you would need to run it a
bunch of times. 10 seemed like a reasonable balance between being enough for
most apps and not being obnoxiously long in terms of output.

You can always customize the count with `--count 3` to generate however many
tokens you want.

### Why did you pick 99 characters as a length?

It's what Stripe uses when generating their API keys. When it comes to security,
the last thing you want to do is guess at stuff or undershoot the length.

Chances are they put in a lot of thought into that value and 99 characters
should not be crackable for many trillions of years!

If you use a prefix, it really comes out to be 99 + the prefix's length too.
The prefix gets prepended to the token after it's been generated with whatever
the length value is.

If 99 isn't enough, you can always customize it with `--length 128`.

### Why did you limit tokens to letters and digits?

Technically Python3 supports generating URL safe tokens that include
underscores and hyphens, but I chose against that because if you decide to
prefix your tokens such as `prod_`, then I didn't want to worry about maybe
wanting to parse those tokens later by splitting on an underscore and then
ending up with more than 2 items in the split list.

That and it's what Stripe does too. Again, you can't go too wrong following
their standards!

## About the author

- Nick Janetakis | <https://nickjanetakis.com> | [@nickjanetakis](https://twitter.com/nickjanetakis)

If you're interested in learning Flask I have a 20+ hour video course called
[Build a SAAS App with
Flask](https://buildasaasappwithflask.com/?utm_source=github&utm_medium=flasksecrets&utm_campaign=readme).
It's a course where we build a real world SAAS app. Everything about the course
and demo videos of what we build is on the site linked above.
