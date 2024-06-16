import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';
import autoprefixer from 'autoprefixer';
import tailwind from 'tailwindcss';
export default {
    // Consult https://svelte.dev/docs#compile-time-svelte-preprocess
    // for more information about preprocessors
    preprocess: [
        vitePreprocess({
            postcss: {
                plugins: [tailwind, autoprefixer],
            },
        }),
    ],
};
