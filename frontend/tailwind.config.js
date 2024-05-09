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
                container: '85vw',
                container_fit: 'calc(100% - 8rem)'
            },
            height: {
                max: '100vh',
                container: '85vh'
            },
            maxHeight: {
                container_fit: 'calc(85vh - 11rem)'
            }
        }
    },
    plugins: [],
};