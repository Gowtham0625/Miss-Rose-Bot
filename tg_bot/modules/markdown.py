__help__ = """
You can use markdown to make your messages more expressive. This is the markdown currently supported:

``code words`` backticks allow you to wrap your words in monospace fonts. Shows as: code words.
`*bold words*` asterisks are used for bold font. Shows as: bold words.
`_italic words_` underscores are used for italics. Shows as: italic words.
`~strikethrough words~` tildes are used for strikethrough. Shows as: strikethrough words.
`__underlined words__` two underscores are used for underlines. Shows as: underlined words. NOTE: Some clients try to be smart and interpret it as italic. In that case, try to use your app's built-in formatting.
`[hyperlink](example.com)` this is used for hyperlinks, and will show as such: [hyperlink](http://example.com/). Make sure not to add any extra spaces between the ] and the ( or it won't be valid markdown.

Now, if you wanted to have buttons on your message, you could use this special syntax:
`[button](buttonurl://example.com)`
This will create a button named "button" which redirects the user to example.com upon clicking.
If you would like to add two buttons on the same row, add :same at the end of your link; it'll set it on the same line as the other one. For example:
```
[button](buttonurl://example.com)
[button 2](buttonurl://example.com:same)
[button 3](buttonurl://example.com)
```
will create two buttons on the same line (buttons 1 and 2), and a last one (button 3) on a second line.
If you want to link a note in the button, simply use the notename as the url, like this:
`[note button](buttonurl://#note)`
The user will then be redirected to the bot PM, and receive the note there - reducing note spam in the chat.

Fillings:
You can also use certain tags to fill your message with user or chat info; the options are:
`{first}`: The user's first name.
`{last}`: The user's last name.
`{fullname}`: The user's full name.
`{username}`: The user's username; if none is available, mentions the user.
`{mention}`: Mentions the user, using their firstname.
`{id}`: The user's id.
`{chatname}`: The chat's name.
`{rules}`: Adds a link to the chat's rules.
`{preview}`: Enables link previews for this message. Can be useful when using links to Instant View pages.

An example of how to use fillings would be to set your welcome, via:
`/setwelcome Hey there {first}! Welcome to {chatname}`.

Try these out on notes, filters, welcome messages or even rules!
"""

__mod_name__ = "Markdown"
