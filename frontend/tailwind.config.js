/** @type {import('tailwindcss').Config} */
export default {
    content: ['./index.html', './src/**/*.{svelte,js,ts,jsx,tsx}'],
    theme: {
        extend: {
            backgroundColor: {
                primary: '#E7E5E4',
                primary_dark: '#181A1B',
            },
            textColor: {
                primary: '#E7E5E4',
                primary_dark: '#181A1B',
            },
            fontFamily: {
                custom: "'Martian Mono', monospace",
            },
            width: {
                container: '85vw',
                container_fit: 'calc(100% - 8rem)',
            },
            height: {
                container: '85vh',
            },
            maxHeight: {
                container_fit: 'calc(85vh - 11rem)',
            },
        },
    },
    darkMode: 'media',
    plugins: [],
};
