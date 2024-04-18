<script lang="ts">
    import { onMount } from 'svelte';
    let saved = false;
    function beforeUnload(e: BeforeUnloadEvent) {
        if (!saved) {
            e.returnValue = false;
        }
    }
    let model = '';
    let prompt = '';
    onMount(() => {
        fetch('/api/config').then((res) => {
            res.json().then((data) => {
                model = data.model;
                prompt = data.prompt;
            });
        });
        window.addEventListener('beforeunload', beforeUnload);
        return () => {
            window.removeEventListener('beforeunload', beforeUnload);
        };
    });
</script>

<div class="flex h-max flex-col items-center justify-center space-y-1">
    <span>Model:</span>
    <select bind:value={model}>
        <option class="text-center">gpt-4-turbo</option>
        <option class="text-center">gpt-4</option>
        <option class="text-center">gpt-3.5-turbo</option>
    </select>
    <span>Prompt:</span>
    <textarea
        class="resize-none rounded-xl border-2 border-black"
        bind:value={prompt}
        rows="10"
    />
    <button
        class="w-60 rounded-xl border-2 border-black"
        on:click={() => {
            fetch('/api/config', {
                method: 'POST',
                body: JSON.stringify({
                    model: model,
                    prompt: prompt,
                }),
            });
            saved = true;
        }}>Save</button
    >
</div>
