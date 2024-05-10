<script lang="ts">
    import { onMount } from 'svelte';
    let model = '';
    let prompt = '';
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
    class="flex h-max flex-col items-center justify-center space-y-1"
    method="POST"
    action="/api/config"
>
    <span>Model:</span>
    <select bind:value={model} name="model" required>
        <option class="text-center">gpt-4-turbo</option>
        <option class="text-center">gpt-4</option>
        <option class="text-center">gpt-3.5-turbo</option>
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
