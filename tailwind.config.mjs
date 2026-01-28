/** @type {import('tailwindcss').Config} */
export default {
    content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
    theme: {
        extend: {
            fontFamily: {
                heading: ['"Outfit"', 'sans-serif'],
                body: ['"Inter"', 'sans-serif'],
            },
            colors: {
                'sea-blue': '#059669', // Modern Emerald/Teal
                'dune-sand': '#e2e8f0', // Cool Slate
                'foam-white': '#ffffff', // Pure White
                'lighthouse-red': '#ef4444',
            },
        },
    },
    plugins: [],
}
