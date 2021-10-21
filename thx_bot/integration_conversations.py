from telegram.ext import CommandHandler
from telegram.ext import ConversationHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler

from thx_bot.commands import CHOOSING
from thx_bot.commands import CHOOSING_ADD_MEMBER
from thx_bot.commands import CHOOSING_REWARDS
from thx_bot.commands import CHOOSING_SIGNUP
from thx_bot.commands import CHOOSING_TOKENS
from thx_bot.commands import CHOOSING_WALLET_UPDATE
from thx_bot.commands import TYPING_REPLY
from thx_bot.commands import TYPING_REPLY_MEMBER
from thx_bot.commands import TYPING_REPLY_SIGNUP
from thx_bot.commands import TYPING_REPLY_WALLET_UPDATE
from thx_bot.commands import TYPING_REWARD_REPLY
from thx_bot.commands import TYPING_TOKENS_REPLY
from thx_bot.commands.add_member import start_adding_member
from thx_bot.commands.add_member import done_member_add
from thx_bot.commands.add_member import received_information_member_add
from thx_bot.commands.add_member import regular_choice_member_add
from thx_bot.commands.create_wallet import done_signup
from thx_bot.commands.create_wallet import received_information_signup
from thx_bot.commands.create_wallet import regular_choice_signup
from thx_bot.commands.create_wallet import start_creating_wallet
from thx_bot.commands.entrance import disable_entrance_checks
from thx_bot.commands.entrance import done_permission
from thx_bot.commands.entrance import permissions_entrypoint
from thx_bot.commands.entrance import received_permission_amount
from thx_bot.commands.entrance import regular_choice_permissions
from thx_bot.commands.entrance import show_entrance_permision_for_channel
from thx_bot.commands.entrance import toggle_users_with_rewards
from thx_bot.commands.pool_rewards import done_rewards
from thx_bot.commands.pool_rewards import pool_show_rewards_command
from thx_bot.commands.pool_rewards import received_information_reward
from thx_bot.commands.pool_rewards import regular_choice_reward
from thx_bot.commands.pool_rewards import rewards_entrypoint
from thx_bot.commands.register_channel import check_connection_channel
from thx_bot.commands.register_channel import done_channel
from thx_bot.commands.register_channel import received_information_channel
from thx_bot.commands.register_channel import regular_choice_channel
from thx_bot.commands.register_channel import start_setting_channel
from thx_bot.commands.update_wallet import done_wallet_update
from thx_bot.commands.update_wallet import received_information_wallet_update
from thx_bot.commands.update_wallet import regular_choice_wallet_update
from thx_bot.commands.update_wallet import start_updating_wallet

register_channel_conversation = ConversationHandler(
    entry_points=[CommandHandler('register_channel', start_setting_channel)],  # noqa
    states={  # noqa
        CHOOSING: [
            MessageHandler(
                Filters.regex('^(Client id|Client secret|Pool address)$'),
                regular_choice_channel
            ),
        ],
        TYPING_REPLY: [
            MessageHandler(
                Filters.text & ~(Filters.command | Filters.regex('^Done$')),
                received_information_channel,
            )
        ],
    },
    fallbacks=[  # noqa
        MessageHandler(Filters.regex('^Done$'), done_channel),
        MessageHandler(Filters.regex('^Test Connection$'), check_connection_channel),
    ],
    name="register_channel",
    persistent=False,
)


create_wallet_conversation = ConversationHandler(
    entry_points=[CommandHandler('create_wallet', start_creating_wallet)],  # noqa
    states={  # noqa
        CHOOSING_SIGNUP: [
            MessageHandler(
                Filters.regex('^(Email|Password)$'), regular_choice_signup
            ),
        ],
        TYPING_REPLY_SIGNUP: [
            MessageHandler(
                Filters.text & ~(Filters.command | Filters.regex('^Done$')),
                received_information_signup,
            )
        ],
    },
    fallbacks=[  # noqa
        MessageHandler(Filters.regex('^Done$'), done_signup),
    ],  # noqa
    name="create_wallet",
    persistent=False,
)


update_wallet_conversation = ConversationHandler(
    entry_points=[CommandHandler('update_wallet', start_updating_wallet)],  # noqa
    states={  # noqa
        CHOOSING_WALLET_UPDATE: [
            MessageHandler(
                Filters.regex('^Wallet Update$'), regular_choice_wallet_update
            ),
        ],
        TYPING_REPLY_WALLET_UPDATE: [
            MessageHandler(
                Filters.text & ~(Filters.command | Filters.regex('^Done$')),
                received_information_wallet_update,
            )
        ],
    },
    fallbacks=[  # noqa
        MessageHandler(Filters.regex('^Done$'), done_wallet_update),
    ],  # noqa
    name="update_wallet",
    persistent=False,
)


rewards_conversation = ConversationHandler(
    entry_points=[CommandHandler('rewards', rewards_entrypoint)],  # noqa
    states={  # noqa
        CHOOSING_REWARDS: [
            MessageHandler(
                Filters.regex('^Set Reward$'), regular_choice_reward
            ),
        ],
        TYPING_REWARD_REPLY: [
            MessageHandler(
                Filters.text & ~(Filters.command | Filters.regex('^Done$')),
                received_information_reward,
            )
        ],
    },
    fallbacks=[  # noqa
        MessageHandler(Filters.regex('^Done$'), done_rewards),
        MessageHandler(Filters.regex('^Show rewards$'), pool_show_rewards_command),
    ],  # noqa
    name="rewards",
    persistent=False,
)

entrance_tokens_conversation = ConversationHandler(
    entry_points=[CommandHandler('entrance', permissions_entrypoint)],
    states={  # noqa
        CHOOSING_TOKENS: [
            MessageHandler(
                Filters.regex('^Set entrance amount$'), regular_choice_permissions
            ),
        ],
        TYPING_TOKENS_REPLY: [
            MessageHandler(
                Filters.text & ~(Filters.command | Filters.regex('^Done$')),
                received_permission_amount,
            )
        ],
    },
    fallbacks=[  # noqa
        MessageHandler(Filters.regex('^Done$'), done_permission),
        MessageHandler(
            Filters.regex('^Show entrance configuration$'), show_entrance_permision_for_channel),
        MessageHandler(
            Filters.regex('^Disable entrance checks$'), disable_entrance_checks),
        MessageHandler(
            Filters.regex('^Toggle only users with rewards$'), toggle_users_with_rewards),
    ],  # noqa
    name="entrance",
    persistent=False,
)

add_member_conversation = ConversationHandler(
    entry_points=[CommandHandler('add_me_to_pool', start_adding_member)],  # noqa
    states={  # noqa
        CHOOSING_ADD_MEMBER: [
            MessageHandler(
                Filters.regex('^Add your wallet$'), regular_choice_member_add
            ),
        ],
        TYPING_REPLY_MEMBER: [
            MessageHandler(
                Filters.text & ~(Filters.command | Filters.regex('^Done$')),
                received_information_member_add,
            )
        ],
    },
    fallbacks=[  # noqa
        MessageHandler(Filters.regex('^Done$'), done_member_add),
    ],  # noqa
    name="add_member",
    persistent=False,
)
