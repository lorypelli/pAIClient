declare global {
    interface Window {
        token: string,
        config: {
            model: string,
            prompt: string
        }
    }
}
export {}