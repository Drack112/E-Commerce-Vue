module.exports = {
  root: true,
  env: {
    browser: true,
    es2021: true
  },
  extends: ['plugin:vue/essential', 'standard'],
  parserOptions: {
    ecmaVersion: 'latest',
    sourceType: 'module'
  },
  plugins: ['vue'],
  rules: {
    'vue/multi-word-component-names': 'off'
  },
  overrides: [
    {
      files: ['src/views/*.vue'],
      rules: {
        'vue/multi-word-component-names': 'off',
        camelcase: 'off',
        'space-before-function-paren': 0
      }
    }
  ]
}
