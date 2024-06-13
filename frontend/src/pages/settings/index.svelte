<script lang="ts">
    import { onMount } from 'svelte';
    let model = '';
    let prompt = '';
    let models = ['gpt-4o', 'gpt-4-turbo', 'gpt-4', 'gpt-3.5-turbo'];
    onMount(() => {
        fetch('/api/config').then((res) => {
            res.json().then((data) => {
                model = data.model;
                prompt = data.prompt;
            });
        });
    });
</script>

<form
    class="flex flex-col items-center justify-center space-y-1"
    method="POST"
    action="/api/config"
>
    <span>Model:</span>
    <select bind:value={model} name="model" required>
        {#each models as m}
            <option class="text-center">{m}</option>
        {/each}
    </select>
    <span>Prompt:</span>
    <textarea
        class="resize-none rounded-xl border-2 border-black"
        bind:value={prompt}
        rows="10"
        name="prompt"
    />
    <button class="w-60 rounded-xl border-2 border-black" type="submit"
        >Save</button
    >
</form>
