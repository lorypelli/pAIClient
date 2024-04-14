import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'
import { multip } from 'vite-plugin-multip'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [svelte(), multip({
    page: {
      title: 'pAIClient'
    }
  })],
})
