/** @type {import('tailwindcss').Config} */
export default {
    content: [
        './index.html',
        './src/**/*.{svelte,js,ts,jsx,tsx}',
    ],
    theme: {
        extend: {
            fontFamily: {
                custom: '\'Martian Mono\', monospace'
            },
            width: {
                container: '1000px',
                container_fit: 'calc(100% - 2rem)'
            },
            height: {
                max: '100vh',
                container: '750px'
            }
        }
    },
    plugins: [],
};