# HOWTO port

- its a sans-io module, no IO included
- its got a callback API recv -> onmessage which Id like to replace
  - plan is then maybe to use a async with API for this handling

- refs
  - https://github.com/mafintosh/simple-message-channels/blob/master/index.js
  - https://github.com/mafintosh/simple-message-channels/blob/master/test.js
  - https://github.com/mafintosh/simple-message-channels/blob/master/example.js
  - https://github.com/mafintosh/simple-message-channels#api
