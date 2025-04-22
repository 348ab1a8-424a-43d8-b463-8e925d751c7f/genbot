using Discord.Commands;
using Discord;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _07cab3d6_0d7d
{
    class CommandServiceConfig
    {
        public bool CaseSensitiveCommands { get; set; }

        public RunMode DefaultRunMode { get; set; }

        public bool IgnoreExtraArgs { get; set; }

        public LogSeverity LogLevel { get; set; }

        public Dictionary<char, char> QuotationMarkAliasMap { get; set; }

        public char SeparatorChar { get; set; }

        public bool ThrowOnError { get; set; }
    }
}
