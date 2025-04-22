using Discord;
using Discord.Net;
using Discord.Webhook;
using Discord.WebSocket;
using Newtonsoft.Json;

namespace _07cab3d6_0d7d
{
    internal class Program
    {
        private static DiscordSocketClient _client;

        public static async Task Main()
        {
            // Initialization
            _client = new DiscordSocketClient();

            var token = JsonConvert.DeserializeObject<IConfiguration>(File.ReadAllText("config.json")).Token;

            await _client.LoginAsync(TokenType.Bot, token);
            await _client.StartAsync();

            await Task.Delay(-1);
        }

        public static Task Log(LogMessage msg)
        {
            Console.WriteLine(msg.ToString());
            return Task.CompletedTask;
        }
    }
}
