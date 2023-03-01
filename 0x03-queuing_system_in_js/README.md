Curriculuum <br>
**Short Specializations** <br>

# 0x03. Queuing System in JS

`Back-end` `JavaScript` `ES6` `Redis` `NodeJS` `ExpressJS` `Kue`

## Resources

* [Redis quick start](https://www.redis.io/docs//getting-started/)
* [Redis client interface](https://www.redis.io/docs/ui/cli/)
* [Redis client for Node JS](https://www.github.com/redis/node-redis)
* [Kue](https://www.github.com/Automattic/kue) _deprecated but still used in the industry_

## Requirements

* Code compiled/interpreted on Ubuntu 18.04, Node 12.x, and Redis 5.0.7
* All file should end with a newline
* Mandatory `README.md` file
* Code use the `js` extension

## Required Files

`package.json`
<details>
  <summary>Click to show/hide file contents</summary>

  ```json
  {
    "name": "queuing_system_in_js",
    "version": "1.0.0",
    "description": "",
    "main": "index.js",
    "scripts": {
      "lint": "./node_modules/.bin/eslint",
      "check-lint": "lint [0-9]*.js",
      "test": "./node_modules/.bin/mocha --require @babel/register --exit",
      "dev": "nodemon --exec babel-node --presets @babel/preset-env"
    },
    "author": "",
    "license": "ISC",
    "dependencies": {
      "chai-http": "^4.3.0",
      "express": "^4.17.1",
      "kue": "^0.11.6",
      "redis": "^2.8.0"
    },
    "devDependencies": {
      "@babel/cli": "^7.8.0",
      "@babel/core": "^7.8.0",
      "@babel/node": "^7.8.0",
      "@babel/preset-env": "^7.8.2",
      "@babel/register": "^7.8.0",
      "eslint": "^6.4.0",
      "eslint-config-airbnb-base": "^14.0.0",
      "eslint-plugin-import": "^2.18.2",
      "eslint-plugin-jest": "^22.17.0",
      "nodemon": "^2.0.2",
      "chai": "^4.2.0",
      "mocha": "^6.2.2",
      "request": "^2.88.0",
      "sinon": "^7.5.0"
    }
  }
  ```
</details>

`.babelrc`
<details>
  <summary>Click to show/hide file contents</summary>

  ```
  {
    "presets": [
      "@babel/presets-env"
    ]
  }
  ```
</details>

## and...

Don't forget to run `$ npm install` when you have the `package.json`

## Finally...
