<script lang="ts">
    let token = '';
</script>

<form
    class="flex flex-col items-center justify-center space-y-1"
    method="POST"
    action="/api/login"
>
    <span>Token:</span>
    <textarea
        class="bg-primary text-primary_dark dark:bg-primary_dark dark:text-primary resize-none rounded-xl border-2 border-black dark:border-white"
        bind:value={token}
        name="token"
        required
    />
    <button
        class="text-primary_dark dark:text-primary w-60 rounded-xl border-2 border-black dark:border-white"
        type="submit">Login</button
    >
    <button
        class="text-primary_dark dark:text-primary w-60 rounded-xl border-2 border-black dark:border-white"
        on:click={() => {
            fetch('/api/env').then((res) => {
                res.text().then((data) => {
                    token = data;
                });
            });
        }}
        type="button">Load from Env</button
    >
</form>
