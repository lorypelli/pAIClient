<script lang="ts">
    let model = '';
    let prompt = '';
    fetch('/api/config').then((res) => {
        res.json().then((data) => {
            model = data.model;
            prompt = data.prompt;
        });
    });
    let models = ['gpt-4o', 'gpt-4-turbo', 'gpt-4', 'gpt-3.5-turbo'];
</script>

<form
    class="flex flex-col items-center justify-center space-y-1"
    method="POST"
    action="/api/config"
>
    <span>Model:</span>
    <select
        class="bg-primary dark:bg-primary_dark"
        bind:value={model}
        name="model"
        required
    >
        {#each models as m}
            <option class="text-center">{m}</option>
        {/each}
    </select>
    <span>Prompt:</span>
    <textarea
        class="resize-none rounded-xl border-2 border-black bg-primary text-primary_dark dark:border-white dark:bg-primary_dark dark:text-primary"
        bind:value={prompt}
        name="prompt"
        rows="10"
    />
    <button
        class="w-60 rounded-xl border-2 border-black dark:border-white"
        type="submit">Save</button
    >
</form>
