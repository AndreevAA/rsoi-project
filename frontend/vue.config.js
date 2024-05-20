const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true, 
  devServer: {
        proxy: {
            "/api/*": {
                target: "http://gateway-service:8080",
                secure: false
            }
        }
    }
})
