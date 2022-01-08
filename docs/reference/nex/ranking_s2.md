
# Module: <code>nintendo.nex.ranking_s2</code>

Provides a client and server for the `RankingProtocolS2`. This page was generated automatically from `ranking_s2.proto`.

<code>**class** [RankingClientS2](#rankingclients2)</code><br>
<span class="docs">The client for the `RankingProtocolS2`.</span>

<code>**class** [RankingServerS2](#rankingservers2)</code><br>
<span class="docs">The server for the `RankingProtocolS2`.</span>

<code>**class** [RankingMode](#rankingmode)</code><br>
<code>**class** [RankingOrderCalc](#rankingordercalc)</code><br>
<code>**class** [RankingStatFlags](#rankingstatflags)</code><br>

<code>**class** [FestivalResult](#festivalresult)([Structure](common.md))</code><br>
<code>**class** [FestivalUploadScoreParam](#festivaluploadscoreparam)([Structure](common.md))</code><br>
<code>**class** [FestivalUploadVoteParam](#festivaluploadvoteparam)([Structure](common.md))</code><br>
<code>**class** [LeaguePlayerDetail](#leagueplayerdetail)([Structure](common.md))</code><br>
<code>**class** [LeaguePointInfo](#leaguepointinfo)([Structure](common.md))</code><br>
<code>**class** [LeagueResult](#leagueresult)([Structure](common.md))</code><br>
<code>**class** [RankingCachedResult](#rankingcachedresult)([RankingResult](#rankingresult))</code><br>
<code>**class** [RankingChangeAttributesParam](#rankingchangeattributesparam)([Structure](common.md))</code><br>
<code>**class** [RankingOrderParam](#rankingorderparam)([Structure](common.md))</code><br>
<code>**class** [RankingRankData](#rankingrankdata)([Structure](common.md))</code><br>
<code>**class** [RankingResult](#rankingresult)([Structure](common.md))</code><br>
<code>**class** [RankingScoreData](#rankingscoredata)([Structure](common.md))</code><br>
<code>**class** [RankingStats](#rankingstats)([Structure](common.md))</code><br>

## RankingClientS2
<code>**def _\_init__**(client: [RMCClient](rmc.md#rmcclient) / [HppClient](hpp.md#hppclient))</code><br>
<span class="docs">Creates a new [`RankingClientS2`](#rankingclients2).</span>

<code>**async def upload_score**(score_data: [RankingScoreData](#rankingscoredata), unique_id: int) -> None</code><br>
<span class="docs">Calls method `1` on the server.</span>

<code>**async def delete_score**(category: int, unique_id: int) -> None</code><br>
<span class="docs">Calls method `2` on the server.</span>

<code>**async def delete_all_scores**(unique_id: int) -> None</code><br>
<span class="docs">Calls method `3` on the server.</span>

<code>**async def upload_common_data**(common_data: bytes, unique_id: int) -> None</code><br>
<span class="docs">Calls method `4` on the server.</span>

<code>**async def delete_common_data**(unique_id: int) -> None</code><br>
<span class="docs">Calls method `5` on the server.</span>

<code>**async def get_common_data**(unique_id: int) -> bytes</code><br>
<span class="docs">Calls method `6` on the server.</span>

<code>**async def change_attributes**(category: int, param: [RankingChangeAttributesParam](#rankingchangeattributesparam), unique_id: int) -> None</code><br>
<span class="docs">Calls method `7` on the server.</span>

<code>**async def change_all_attributes**(param: [RankingChangeAttributesParam](#rankingchangeattributesparam), unique_id: int) -> None</code><br>
<span class="docs">Calls method `8` on the server.</span>

<code>**async def get_ranking**(mode: int, category: int, order: [RankingOrderParam](#rankingorderparam), unique_id: int, pid: int) -> [RankingResult](#rankingresult)</code><br>
<span class="docs">Calls method `9` on the server.</span>

<code>**async def get_approx_order**(category: int, order: [RankingOrderParam](#rankingorderparam), score: int, unique_id: int, pid: int) -> int</code><br>
<span class="docs">Calls method `10` on the server.</span>

<code>**async def get_stats**(category: int, order: [RankingOrderParam](#rankingorderparam), flags: int) -> [RankingStats](#rankingstats)</code><br>
<span class="docs">Calls method `11` on the server.</span>

<code>**async def get_ranking_by_pid_list**(pids: list[int], mode: int, category: int, order: [RankingOrderParam](#rankingorderparam), unique_id: int) -> [RankingResult](#rankingresult)</code><br>
<span class="docs">Calls method `12` on the server.</span>

<code>**async def get_ranking_by_unique_id_list**(ids: list[int], mode: int, category: int, order: [RankingOrderParam](#rankingorderparam), unique_id: int) -> [RankingResult](#rankingresult)</code><br>
<span class="docs">Calls method `13` on the server.</span>

<code>**async def get_cached_topx_ranking**(category: int, order: [RankingOrderParam](#rankingorderparam)) -> [RankingCachedResult](#rankingcachedresult)</code><br>
<span class="docs">Calls method `14` on the server.</span>

<code>**async def get_cached_topx_rankings**(categories: list[int], order: list[[RankingOrderParam](#rankingorderparam)]) -> list[[RankingCachedResult](#rankingcachedresult)]</code><br>
<span class="docs">Calls method `15` on the server.</span>

<code>**async def upload_league_point**(info: [LeaguePointInfo](#leaguepointinfo)) -> None</code><br>
<span class="docs">Calls method `16` on the server.</span>

<code>**async def get_league_result**(league_id: str, tag_id: int) -> [LeagueResult](#leagueresult)</code><br>
<span class="docs">Calls method `17` on the server.</span>

<code>**async def get_festival_result**(festival_id: int) -> [FestivalResult](#festivalresult)</code><br>
<span class="docs">Calls method `18` on the server.</span>

<code>**async def upload_festival_vote**(upload_param: [FestivalUploadVoteParam](#festivaluploadvoteparam)) -> None</code><br>
<span class="docs">Calls method `19` on the server.</span>

<code>**async def upload_festival_score**(upload_param: [FestivalUploadScoreParam](#festivaluploadscoreparam)) -> None</code><br>
<span class="docs">Calls method `20` on the server.</span>

<code>**async def delete_festival**(festival_id: int) -> None</code><br>
<span class="docs">Calls method `21` on the server.</span>

## RankingServerS2
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new [`RankingServerS2`](#rankingservers2).</span>

<code>**async def logout**(client: [RMCClient](rmc.md#rmcclient)) -> None</code><br>
<span class="docs">Called whenever a client is disconnected. May be overridden by a subclass.</span>

<code>**async def upload_score**(client: [RMCClient](rmc.md#rmcclient), score_data: [RankingScoreData](#rankingscoredata), unique_id: int) -> None</code><br>
<span class="docs">Handler for method `1`. This method should be overridden by a subclass.</span>

<code>**async def delete_score**(client: [RMCClient](rmc.md#rmcclient), category: int, unique_id: int) -> None</code><br>
<span class="docs">Handler for method `2`. This method should be overridden by a subclass.</span>

<code>**async def delete_all_scores**(client: [RMCClient](rmc.md#rmcclient), unique_id: int) -> None</code><br>
<span class="docs">Handler for method `3`. This method should be overridden by a subclass.</span>

<code>**async def upload_common_data**(client: [RMCClient](rmc.md#rmcclient), common_data: bytes, unique_id: int) -> None</code><br>
<span class="docs">Handler for method `4`. This method should be overridden by a subclass.</span>

<code>**async def delete_common_data**(client: [RMCClient](rmc.md#rmcclient), unique_id: int) -> None</code><br>
<span class="docs">Handler for method `5`. This method should be overridden by a subclass.</span>

<code>**async def get_common_data**(client: [RMCClient](rmc.md#rmcclient), unique_id: int) -> bytes</code><br>
<span class="docs">Handler for method `6`. This method should be overridden by a subclass.</span>

<code>**async def change_attributes**(client: [RMCClient](rmc.md#rmcclient), category: int, param: [RankingChangeAttributesParam](#rankingchangeattributesparam), unique_id: int) -> None</code><br>
<span class="docs">Handler for method `7`. This method should be overridden by a subclass.</span>

<code>**async def change_all_attributes**(client: [RMCClient](rmc.md#rmcclient), param: [RankingChangeAttributesParam](#rankingchangeattributesparam), unique_id: int) -> None</code><br>
<span class="docs">Handler for method `8`. This method should be overridden by a subclass.</span>

<code>**async def get_ranking**(client: [RMCClient](rmc.md#rmcclient), mode: int, category: int, order: [RankingOrderParam](#rankingorderparam), unique_id: int, pid: int) -> [RankingResult](#rankingresult)</code><br>
<span class="docs">Handler for method `9`. This method should be overridden by a subclass.</span>

<code>**async def get_approx_order**(client: [RMCClient](rmc.md#rmcclient), category: int, order: [RankingOrderParam](#rankingorderparam), score: int, unique_id: int, pid: int) -> int</code><br>
<span class="docs">Handler for method `10`. This method should be overridden by a subclass.</span>

<code>**async def get_stats**(client: [RMCClient](rmc.md#rmcclient), category: int, order: [RankingOrderParam](#rankingorderparam), flags: int) -> [RankingStats](#rankingstats)</code><br>
<span class="docs">Handler for method `11`. This method should be overridden by a subclass.</span>

<code>**async def get_ranking_by_pid_list**(client: [RMCClient](rmc.md#rmcclient), pids: list[int], mode: int, category: int, order: [RankingOrderParam](#rankingorderparam), unique_id: int) -> [RankingResult](#rankingresult)</code><br>
<span class="docs">Handler for method `12`. This method should be overridden by a subclass.</span>

<code>**async def get_ranking_by_unique_id_list**(client: [RMCClient](rmc.md#rmcclient), ids: list[int], mode: int, category: int, order: [RankingOrderParam](#rankingorderparam), unique_id: int) -> [RankingResult](#rankingresult)</code><br>
<span class="docs">Handler for method `13`. This method should be overridden by a subclass.</span>

<code>**async def get_cached_topx_ranking**(client: [RMCClient](rmc.md#rmcclient), category: int, order: [RankingOrderParam](#rankingorderparam)) -> [RankingCachedResult](#rankingcachedresult)</code><br>
<span class="docs">Handler for method `14`. This method should be overridden by a subclass.</span>

<code>**async def get_cached_topx_rankings**(client: [RMCClient](rmc.md#rmcclient), categories: list[int], order: list[[RankingOrderParam](#rankingorderparam)]) -> list[[RankingCachedResult](#rankingcachedresult)]</code><br>
<span class="docs">Handler for method `15`. This method should be overridden by a subclass.</span>

<code>**async def upload_league_point**(client: [RMCClient](rmc.md#rmcclient), info: [LeaguePointInfo](#leaguepointinfo)) -> None</code><br>
<span class="docs">Handler for method `16`. This method should be overridden by a subclass.</span>

<code>**async def get_league_result**(client: [RMCClient](rmc.md#rmcclient), league_id: str, tag_id: int) -> [LeagueResult](#leagueresult)</code><br>
<span class="docs">Handler for method `17`. This method should be overridden by a subclass.</span>

<code>**async def get_festival_result**(client: [RMCClient](rmc.md#rmcclient), festival_id: int) -> [FestivalResult](#festivalresult)</code><br>
<span class="docs">Handler for method `18`. This method should be overridden by a subclass.</span>

<code>**async def upload_festival_vote**(client: [RMCClient](rmc.md#rmcclient), upload_param: [FestivalUploadVoteParam](#festivaluploadvoteparam)) -> None</code><br>
<span class="docs">Handler for method `19`. This method should be overridden by a subclass.</span>

<code>**async def upload_festival_score**(client: [RMCClient](rmc.md#rmcclient), upload_param: [FestivalUploadScoreParam](#festivaluploadscoreparam)) -> None</code><br>
<span class="docs">Handler for method `20`. This method should be overridden by a subclass.</span>

<code>**async def delete_festival**(client: [RMCClient](rmc.md#rmcclient), festival_id: int) -> None</code><br>
<span class="docs">Handler for method `21`. This method should be overridden by a subclass.</span>

## RankingMode
This class defines the following constants:<br>
<span class="docs">
`GLOBAL = 0`<br>
`GLOBAL_AROUND_SELF = 1`<br>
`SELF = 4`<br>
</span>

## RankingOrderCalc
This class defines the following constants:<br>
<span class="docs">
`STANDARD = 0`<br>
`ORDINAL = 1`<br>
</span>

## RankingStatFlags
This class defines the following constants:<br>
<span class="docs">
`RANKING_COUNT = 1`<br>
`TOTAL_SCORE = 2`<br>
`LOWEST_SCORE = 4`<br>
`HIGHEST_SCORE = 8`<br>
`AVERAGE_SCORE = 16`<br>
`ALL = 31`<br>
</span>

## FestivalResult
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `FestivalResult` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>festival_id: int</code><br>
<code>num_participants: int</code><br>
<code>team_participants: list[int]</code><br>
<code>team_scores: list[int]</code><br>
<code>updated_time: [DateTime](common.md#datetime)</code><br>
</span><br>

## FestivalUploadScoreParam
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `FestivalUploadScoreParam` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>unique_id: int</code><br>
<code>region: int</code><br>
<code>festival_id: int</code><br>
<code>team_id: int</code><br>
<code>score: int</code><br>
<code>battle_gathering_id: int</code><br>
<code>battle_result: int</code><br>
<code>application_buffer: bytes</code><br>
</span><br>

## FestivalUploadVoteParam
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `FestivalUploadVoteParam` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>festival_id: int</code><br>
<code>theme_id: int</code><br>
</span><br>

## LeaguePlayerDetail
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `LeaguePlayerDetail` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>principal_id: int</code><br>
<code>weapon_id: int</code><br>
</span><br>

## LeaguePointInfo
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `LeaguePointInfo` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>tag_id: int</code><br>
<code>region_flag: int</code><br>
<code>league_id: str</code><br>
<code>point: int</code><br>
<code>tag_members: dict[int, [LeaguePlayerDetail](#leagueplayerdetail)]</code><br>
<code>application_buffer: bytes</code><br>
</span><br>

## LeagueResult
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `LeagueResult` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>league_point_info: [LeaguePointInfo](#leaguepointinfo) = [LeaguePointInfo](#leaguepointinfo)()</code><br>
<code>status: int</code><br>
<code>specific_rank: int</code><br>
<code>rank_ratio: int</code><br>
<code>tag_num: int</code><br>
<code>match_count: int</code><br>
</span><br>

## RankingCachedResult
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `RankingCachedResult` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>created_time: [DateTime](common.md#datetime)</code><br>
<code>expired_time: [DateTime](common.md#datetime)</code><br>
<code>max_length: int</code><br>
</span><br>

## RankingChangeAttributesParam
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `RankingChangeAttributesParam` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>flags: int</code><br>
<code>groups: list[int]</code><br>
<code>param: int</code><br>
</span><br>

## RankingOrderParam
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `RankingOrderParam` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>order_calc: int = 0</code><br>
<code>group_index: int = 255</code><br>
<code>group_num: int = 0</code><br>
<code>time_scope: int = 2</code><br>
<code>offset: int</code><br>
<code>count: int</code><br>
</span><br>

## RankingRankData
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `RankingRankData` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>pid: int</code><br>
<code>unique_id: int</code><br>
<code>rank: int</code><br>
<code>category: int</code><br>
<code>score: int</code><br>
<code>groups: list[int]</code><br>
<code>param: int</code><br>
<code>common_data: bytes</code><br>
If `nex.version` >= 40000:<br>
<span class="docs">
<code>update_time: [DateTime](common.md#datetime)</code><br>
</span><br>
</span><br>

## RankingResult
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `RankingResult` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>data: list[[RankingRankData](#rankingrankdata)]</code><br>
<code>total: int</code><br>
<code>since_time: [DateTime](common.md#datetime)</code><br>
</span><br>

## RankingScoreData
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `RankingScoreData` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>category: int</code><br>
<code>score: int</code><br>
<code>order: int</code><br>
<code>update_mode: int</code><br>
<code>groups: list[int]</code><br>
<code>param: int</code><br>
</span><br>

## RankingStats
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `RankingStats` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>stats: list[float]</code><br>
</span><br>
