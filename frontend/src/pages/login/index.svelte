<script lang="ts">
    let token = '';
</script>

<form
    class="flex h-max flex-col items-center justify-center space-y-1"
    method="POST"
    action="/api/login"
>
    <span>Token:</span>
    <textarea
        class="resize-none rounded-xl border-2 border-black"
        bind:value={token}
        name="token"
        required
    />
    <button class="w-60 rounded-xl border-2 border-black" type="submit"
        >Login</button
    >
    <button
        class="w-60 rounded-xl border-2 border-black"
        on:click={() => {
            fetch('/api/env').then((res) => {
                res.text().then((data) => {
                    token = data;
                });
            });
        }}>Load from Env</button
    >
</form>
