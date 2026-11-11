import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react'

// Yerelde `npm run dev` sırasında /api/chat isteğini Vercel fonksiyonuyla aynı koda yönlendirir.
// Anahtarlar web/.env.local dosyasından okunur (git'e girmez).
function localApi() {
  return {
    name: 'local-api',
    configureServer(server) {
      Object.assign(process.env, loadEnv('development', process.cwd(), ''))
      server.middlewares.use('/api/chat', async (req, res) => {
        const chunks = []
        for await (const c of req) chunks.push(c)
        const { POST } = await server.ssrLoadModule('/api/chat.js')
        const request = new Request(`http://${req.headers.host}${req.originalUrl}`, {
          method: req.method,
          headers: { 'content-type': req.headers['content-type'] || 'application/json' },
          body: req.method === 'POST' ? Buffer.concat(chunks) : undefined,
        })
        const response = await POST(request)
        res.statusCode = response.status
        response.headers.forEach((v, k) => res.setHeader(k, v))
        res.end(await response.text())
      })
    },
  }
}

export default defineConfig({
  plugins: [react(), localApi()],
})
