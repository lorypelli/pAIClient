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
        class="resize-none rounded-xl border-2 border-black bg-primary text-primary_dark dark:border-white dark:bg-primary_dark dark:text-primary"
        bind:value={token}
        name="token"
        required
    />
    <button
        class="w-60 rounded-xl border-2 border-black text-primary_dark dark:border-white dark:text-primary"
        type="submit">Login</button
    >
    <button
        class="w-60 rounded-xl border-2 border-black text-primary_dark dark:border-white dark:text-primary"
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
