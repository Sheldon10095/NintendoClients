
# Module: <code>nintendo.nex.datastore_s2</code>

Provides a client and server for the `DataStoreProtocolS2`. This page was generated automatically from `datastore_s2.proto`.

<code>**class** [DataStoreClientS2](#datastoreclients2)</code><br>
<span class="docs">The client for the `DataStoreProtocolS2`.</span>

<code>**class** [DataStoreServerS2](#datastoreservers2)</code><br>
<span class="docs">The server for the `DataStoreProtocolS2`.</span>

<code>**class** [CalicoFesStats](#calicofesstats)([CalicoRegularStats](#calicoregularstats))</code><br>
<code>**class** [CalicoFesStatsV2](#calicofesstatsv2)([CalicoFesStats](#calicofesstats))</code><br>
<code>**class** [CalicoGachiStats](#calicogachistats)([CalicoStatsBase](#calicostatsbase))</code><br>
<code>**class** [CalicoLeagueStats](#calicoleaguestats)([CalicoGachiStats](#calicogachistats))</code><br>
<code>**class** [CalicoPlayerResult](#calicoplayerresult)([Structure](common.md))</code><br>
<code>**class** [CalicoPlayerSimple](#calicoplayersimple)([Structure](common.md))</code><br>
<code>**class** [CalicoRegularStats](#calicoregularstats)([CalicoStatsBase](#calicostatsbase))</code><br>
<code>**class** [CalicoStatsBase](#calicostatsbase)([Structure](common.md))</code><br>
<code>**class** [CalicoXStats](#calicoxstats)([CalicoGachiStats](#calicogachistats))</code><br>
<code>**class** [CoconutGetInfo](#coconutgetinfo)([Structure](common.md))</code><br>
<code>**class** [CoconutGetParam](#coconutgetparam)([Structure](common.md))</code><br>
<code>**class** [CoconutMeta](#coconutmeta)([Structure](common.md))</code><br>
<code>**class** [CoconutViolation](#coconutviolation)([Structure](common.md))</code><br>
<code>**class** [DataStoreChangeMetaCompareParam](#datastorechangemetacompareparam)([Structure](common.md))</code><br>
<code>**class** [DataStoreChangeMetaParam](#datastorechangemetaparam)([Structure](common.md))</code><br>
<code>**class** [DataStoreChangeMetaParamV1](#datastorechangemetaparamv1)([Structure](common.md))</code><br>
<code>**class** [DataStoreCompletePostParam](#datastorecompletepostparam)([Structure](common.md))</code><br>
<code>**class** [DataStoreCompletePostParamV1](#datastorecompletepostparamv1)([Structure](common.md))</code><br>
<code>**class** [DataStoreCompleteUpdateParam](#datastorecompleteupdateparam)([Structure](common.md))</code><br>
<code>**class** [DataStoreDeleteParam](#datastoredeleteparam)([Structure](common.md))</code><br>
<code>**class** [DataStoreGetMetaParam](#datastoregetmetaparam)([Structure](common.md))</code><br>
<code>**class** [DataStoreGetNewArrivedNotificationsParam](#datastoregetnewarrivednotificationsparam)([Structure](common.md))</code><br>
<code>**class** [DataStoreGetNotificationUrlParam](#datastoregetnotificationurlparam)([Structure](common.md))</code><br>
<code>**class** [DataStoreGetSpecificMetaParam](#datastoregetspecificmetaparam)([Structure](common.md))</code><br>
<code>**class** [DataStoreGetSpecificMetaParamV1](#datastoregetspecificmetaparamv1)([Structure](common.md))</code><br>
<code>**class** [DataStoreKeyValue](#datastorekeyvalue)([Structure](common.md))</code><br>
<code>**class** [DataStoreMetaInfo](#datastoremetainfo)([Structure](common.md))</code><br>
<code>**class** [DataStoreNotification](#datastorenotification)([Structure](common.md))</code><br>
<code>**class** [DataStoreNotificationV1](#datastorenotificationv1)([Structure](common.md))</code><br>
<code>**class** [DataStorePasswordInfo](#datastorepasswordinfo)([Structure](common.md))</code><br>
<code>**class** [DataStorePermission](#datastorepermission)([Structure](common.md))</code><br>
<code>**class** [DataStorePersistenceInfo](#datastorepersistenceinfo)([Structure](common.md))</code><br>
<code>**class** [DataStorePersistenceInitParam](#datastorepersistenceinitparam)([Structure](common.md))</code><br>
<code>**class** [DataStorePersistenceTarget](#datastorepersistencetarget)([Structure](common.md))</code><br>
<code>**class** [DataStorePrepareGetParam](#datastorepreparegetparam)([Structure](common.md))</code><br>
<code>**class** [DataStorePrepareGetParamV1](#datastorepreparegetparamv1)([Structure](common.md))</code><br>
<code>**class** [DataStorePreparePostParam](#datastorepreparepostparam)([Structure](common.md))</code><br>
<code>**class** [DataStorePreparePostParamV1](#datastorepreparepostparamv1)([Structure](common.md))</code><br>
<code>**class** [DataStorePrepareUpdateParam](#datastoreprepareupdateparam)([Structure](common.md))</code><br>
<code>**class** [DataStoreRateObjectParam](#datastorerateobjectparam)([Structure](common.md))</code><br>
<code>**class** [DataStoreRatingInfo](#datastoreratinginfo)([Structure](common.md))</code><br>
<code>**class** [DataStoreRatingInfoWithSlot](#datastoreratinginfowithslot)([Structure](common.md))</code><br>
<code>**class** [DataStoreRatingInitParam](#datastoreratinginitparam)([Structure](common.md))</code><br>
<code>**class** [DataStoreRatingInitParamWithSlot](#datastoreratinginitparamwithslot)([Structure](common.md))</code><br>
<code>**class** [DataStoreRatingLog](#datastoreratinglog)([Structure](common.md))</code><br>
<code>**class** [DataStoreRatingTarget](#datastoreratingtarget)([Structure](common.md))</code><br>
<code>**class** [DataStoreReqGetAdditionalMeta](#datastorereqgetadditionalmeta)([Structure](common.md))</code><br>
<code>**class** [DataStoreReqGetInfo](#datastorereqgetinfo)([Structure](common.md))</code><br>
<code>**class** [DataStoreReqGetInfoV1](#datastorereqgetinfov1)([Structure](common.md))</code><br>
<code>**class** [DataStoreReqGetNotificationUrlInfo](#datastorereqgetnotificationurlinfo)([Structure](common.md))</code><br>
<code>**class** [DataStoreReqPostInfo](#datastorereqpostinfo)([Structure](common.md))</code><br>
<code>**class** [DataStoreReqPostInfoV1](#datastorereqpostinfov1)([Structure](common.md))</code><br>
<code>**class** [DataStoreReqUpdateInfo](#datastorerequpdateinfo)([Structure](common.md))</code><br>
<code>**class** [DataStoreSearchParam](#datastoresearchparam)([Structure](common.md))</code><br>
<code>**class** [DataStoreSearchResult](#datastoresearchresult)([Structure](common.md))</code><br>
<code>**class** [DataStoreSpecificMetaInfo](#datastorespecificmetainfo)([Structure](common.md))</code><br>
<code>**class** [DataStoreSpecificMetaInfoV1](#datastorespecificmetainfov1)([Structure](common.md))</code><br>
<code>**class** [DataStoreTouchObjectParam](#datastoretouchobjectparam)([Structure](common.md))</code><br>
<code>**class** [OrderedInfo](#orderedinfo)([Structure](common.md))</code><br>
<code>**class** [PlayLogEntry](#playlogentry)([Structure](common.md))</code><br>
<code>**class** [PlayLogPrepareGetParam](#playlogpreparegetparam)([Structure](common.md))</code><br>
<code>**class** [PlayLogPreparePostParam](#playlogpreparepostparam)([Structure](common.md))</code><br>
<code>**class** [StageTimeAttackInfo](#stagetimeattackinfo)([Structure](common.md))</code><br>
<code>**class** [StageTimeAttackWeapon](#stagetimeattackweapon)([Structure](common.md))</code><br>
<code>**class** [TimeAttackInfo](#timeattackinfo)([Structure](common.md))</code><br>

## DataStoreClientS2
<code>**def _\_init__**(client: [RMCClient](rmc.md#rmcclient) / [HppClient](hpp.md#hppclient))</code><br>
<span class="docs">Creates a new [`DataStoreClientS2`](#datastoreclients2).</span>

<code>**async def prepare_get_object_v1**(param: [DataStorePrepareGetParamV1](#datastorepreparegetparamv1)) -> [DataStoreReqGetInfoV1](#datastorereqgetinfov1)</code><br>
<span class="docs">Calls method `1` on the server.</span>

<code>**async def prepare_post_object_v1**(param: [DataStorePreparePostParamV1](#datastorepreparepostparamv1)) -> [DataStoreReqPostInfoV1](#datastorereqpostinfov1)</code><br>
<span class="docs">Calls method `2` on the server.</span>

<code>**async def complete_post_object_v1**(param: [DataStoreCompletePostParamV1](#datastorecompletepostparamv1)) -> None</code><br>
<span class="docs">Calls method `3` on the server.</span>

<code>**async def delete_object**(param: [DataStoreDeleteParam](#datastoredeleteparam)) -> None</code><br>
<span class="docs">Calls method `4` on the server.</span>

<code>**async def delete_objects**(param: list[[DataStoreDeleteParam](#datastoredeleteparam)], transactional: bool) -> list[[Result](common.md#result)]</code><br>
<span class="docs">Calls method `5` on the server.</span>

<code>**async def change_meta_v1**(param: [DataStoreChangeMetaParamV1](#datastorechangemetaparamv1)) -> None</code><br>
<span class="docs">Calls method `6` on the server.</span>

<code>**async def change_metas_v1**(data_ids: list[int], param: list[[DataStoreChangeMetaParamV1](#datastorechangemetaparamv1)], transactional: bool) -> list[[Result](common.md#result)]</code><br>
<span class="docs">Calls method `7` on the server.</span>

<code>**async def get_meta**(param: [DataStoreGetMetaParam](#datastoregetmetaparam)) -> [DataStoreMetaInfo](#datastoremetainfo)</code><br>
<span class="docs">Calls method `8` on the server.</span>

<code>**async def get_metas**(data_ids: list[int], param: [DataStoreGetMetaParam](#datastoregetmetaparam)) -> [RMCResponse](common.md)</code><br>
<span class="docs">Calls method `9` on the server. The RMC response has the following attributes:<br>
<span class="docs">
<code>info: list[[DataStoreMetaInfo](#datastoremetainfo)]</code><br>
<code>results: list[[Result](common.md#result)]</code><br>
</span>
</span>

<code>**async def prepare_update_object**(param: [DataStorePrepareUpdateParam](#datastoreprepareupdateparam)) -> [DataStoreReqUpdateInfo](#datastorerequpdateinfo)</code><br>
<span class="docs">Calls method `10` on the server.</span>

<code>**async def complete_update_object**(param: [DataStoreCompleteUpdateParam](#datastorecompleteupdateparam)) -> None</code><br>
<span class="docs">Calls method `11` on the server.</span>

<code>**async def search_object**(param: [DataStoreSearchParam](#datastoresearchparam)) -> [DataStoreSearchResult](#datastoresearchresult)</code><br>
<span class="docs">Calls method `12` on the server.</span>

<code>**async def get_notification_url**(param: [DataStoreGetNotificationUrlParam](#datastoregetnotificationurlparam)) -> [DataStoreReqGetNotificationUrlInfo](#datastorereqgetnotificationurlinfo)</code><br>
<span class="docs">Calls method `13` on the server.</span>

<code>**async def get_new_arrived_notifications_v1**(param: [DataStoreGetNewArrivedNotificationsParam](#datastoregetnewarrivednotificationsparam)) -> [RMCResponse](common.md)</code><br>
<span class="docs">Calls method `14` on the server. The RMC response has the following attributes:<br>
<span class="docs">
<code>result: list[[DataStoreNotificationV1](#datastorenotificationv1)]</code><br>
<code>has_next: bool</code><br>
</span>
</span>

<code>**async def rate_object**(target: [DataStoreRatingTarget](#datastoreratingtarget), param: [DataStoreRateObjectParam](#datastorerateobjectparam), fetch_ratings: bool) -> [DataStoreRatingInfo](#datastoreratinginfo)</code><br>
<span class="docs">Calls method `15` on the server.</span>

<code>**async def get_rating**(target: [DataStoreRatingTarget](#datastoreratingtarget), access_password: int) -> [DataStoreRatingInfo](#datastoreratinginfo)</code><br>
<span class="docs">Calls method `16` on the server.</span>

<code>**async def get_ratings**(data_ids: list[int], access_password: int) -> [RMCResponse](common.md)</code><br>
<span class="docs">Calls method `17` on the server. The RMC response has the following attributes:<br>
<span class="docs">
<code>ratings: list[list[[DataStoreRatingInfoWithSlot](#datastoreratinginfowithslot)]]</code><br>
<code>results: list[[Result](common.md#result)]</code><br>
</span>
</span>

<code>**async def reset_rating**(target: [DataStoreRatingTarget](#datastoreratingtarget), update_password: int) -> None</code><br>
<span class="docs">Calls method `18` on the server.</span>

<code>**async def reset_ratings**(data_ids: list[int], transactional: bool) -> list[[Result](common.md#result)]</code><br>
<span class="docs">Calls method `19` on the server.</span>

<code>**async def get_specific_meta_v1**(param: [DataStoreGetSpecificMetaParamV1](#datastoregetspecificmetaparamv1)) -> list[[DataStoreSpecificMetaInfoV1](#datastorespecificmetainfov1)]</code><br>
<span class="docs">Calls method `20` on the server.</span>

<code>**async def post_meta_binary**(param: [DataStorePreparePostParam](#datastorepreparepostparam)) -> int</code><br>
<span class="docs">Calls method `21` on the server.</span>

<code>**async def touch_object**(param: [DataStoreTouchObjectParam](#datastoretouchobjectparam)) -> None</code><br>
<span class="docs">Calls method `22` on the server.</span>

<code>**async def get_rating_with_log**(target: [DataStoreRatingTarget](#datastoreratingtarget), access_password: int) -> [RMCResponse](common.md)</code><br>
<span class="docs">Calls method `23` on the server. The RMC response has the following attributes:<br>
<span class="docs">
<code>rating: [DataStoreRatingInfo](#datastoreratinginfo)</code><br>
<code>log: [DataStoreRatingLog](#datastoreratinglog)</code><br>
</span>
</span>

<code>**async def prepare_post_object**(param: [DataStorePreparePostParam](#datastorepreparepostparam)) -> [DataStoreReqPostInfo](#datastorereqpostinfo)</code><br>
<span class="docs">Calls method `24` on the server.</span>

<code>**async def prepare_get_object**(param: [DataStorePrepareGetParam](#datastorepreparegetparam)) -> [DataStoreReqGetInfo](#datastorereqgetinfo)</code><br>
<span class="docs">Calls method `25` on the server.</span>

<code>**async def complete_post_object**(param: [DataStoreCompletePostParam](#datastorecompletepostparam)) -> None</code><br>
<span class="docs">Calls method `26` on the server.</span>

<code>**async def get_new_arrived_notifications**(param: [DataStoreGetNewArrivedNotificationsParam](#datastoregetnewarrivednotificationsparam)) -> [RMCResponse](common.md)</code><br>
<span class="docs">Calls method `27` on the server. The RMC response has the following attributes:<br>
<span class="docs">
<code>result: list[[DataStoreNotification](#datastorenotification)]</code><br>
<code>has_next: bool</code><br>
</span>
</span>

<code>**async def get_specific_meta**(param: [DataStoreGetSpecificMetaParam](#datastoregetspecificmetaparam)) -> list[[DataStoreSpecificMetaInfo](#datastorespecificmetainfo)]</code><br>
<span class="docs">Calls method `28` on the server.</span>

<code>**async def get_persistence_info**(owner_id: int, slot_id: int) -> [DataStorePersistenceInfo](#datastorepersistenceinfo)</code><br>
<span class="docs">Calls method `29` on the server.</span>

<code>**async def get_persistence_infos**(owner_id: int, slot_ids: list[int]) -> [RMCResponse](common.md)</code><br>
<span class="docs">Calls method `30` on the server. The RMC response has the following attributes:<br>
<span class="docs">
<code>infos: list[[DataStorePersistenceInfo](#datastorepersistenceinfo)]</code><br>
<code>results: list[[Result](common.md#result)]</code><br>
</span>
</span>

<code>**async def perpetuate_object**(persistence_slot_id: int, data_id: int, delete_last_object: bool) -> None</code><br>
<span class="docs">Calls method `31` on the server.</span>

<code>**async def unperpetuate_object**(persistence_slot_id: int, delete_last_object: bool) -> None</code><br>
<span class="docs">Calls method `32` on the server.</span>

<code>**async def prepare_get_object_or_meta_binary**(param: [DataStorePrepareGetParam](#datastorepreparegetparam)) -> [RMCResponse](common.md)</code><br>
<span class="docs">Calls method `33` on the server. The RMC response has the following attributes:<br>
<span class="docs">
<code>get_info: [DataStoreReqGetInfo](#datastorereqgetinfo)</code><br>
<code>additional_meta: [DataStoreReqGetAdditionalMeta](#datastorereqgetadditionalmeta)</code><br>
</span>
</span>

<code>**async def get_password_info**(data_id: int) -> [DataStorePasswordInfo](#datastorepasswordinfo)</code><br>
<span class="docs">Calls method `34` on the server.</span>

<code>**async def get_password_infos**(data_ids: list[int]) -> [RMCResponse](common.md)</code><br>
<span class="docs">Calls method `35` on the server. The RMC response has the following attributes:<br>
<span class="docs">
<code>infos: list[[DataStorePasswordInfo](#datastorepasswordinfo)]</code><br>
<code>results: list[[Result](common.md#result)]</code><br>
</span>
</span>

<code>**async def get_metas_multiple_param**(params: list[[DataStoreGetMetaParam](#datastoregetmetaparam)]) -> [RMCResponse](common.md)</code><br>
<span class="docs">Calls method `36` on the server. The RMC response has the following attributes:<br>
<span class="docs">
<code>infos: list[[DataStoreMetaInfo](#datastoremetainfo)]</code><br>
<code>results: list[[Result](common.md#result)]</code><br>
</span>
</span>

<code>**async def complete_post_objects**(data_ids: list[int]) -> None</code><br>
<span class="docs">Calls method `37` on the server.</span>

<code>**async def change_meta**(param: [DataStoreChangeMetaParam](#datastorechangemetaparam)) -> None</code><br>
<span class="docs">Calls method `38` on the server.</span>

<code>**async def change_metas**(data_ids: list[int], param: list[[DataStoreChangeMetaParam](#datastorechangemetaparam)], transactional: bool) -> list[[Result](common.md#result)]</code><br>
<span class="docs">Calls method `39` on the server.</span>

<code>**async def rate_objects**(targets: list[[DataStoreRatingTarget](#datastoreratingtarget)], param: list[[DataStoreRateObjectParam](#datastorerateobjectparam)], transactional: bool, fetch_ratings: bool) -> [RMCResponse](common.md)</code><br>
<span class="docs">Calls method `40` on the server. The RMC response has the following attributes:<br>
<span class="docs">
<code>infos: list[[DataStoreRatingInfo](#datastoreratinginfo)]</code><br>
<code>results: list[[Result](common.md#result)]</code><br>
</span>
</span>

<code>**async def post_meta_binary_with_data_id**(data_id: int, param: [DataStorePreparePostParam](#datastorepreparepostparam)) -> None</code><br>
<span class="docs">Calls method `41` on the server.</span>

<code>**async def post_meta_binaries_with_data_id**(data_ids: list[int], param: list[[DataStorePreparePostParam](#datastorepreparepostparam)], transactional: bool) -> list[[Result](common.md#result)]</code><br>
<span class="docs">Calls method `42` on the server.</span>

<code>**async def rate_object_with_posting**(target: [DataStoreRatingTarget](#datastoreratingtarget), rate_param: [DataStoreRateObjectParam](#datastorerateobjectparam), post_param: [DataStorePreparePostParam](#datastorepreparepostparam), fetch_ratings: bool) -> [DataStoreRatingInfo](#datastoreratinginfo)</code><br>
<span class="docs">Calls method `43` on the server.</span>

<code>**async def rate_objects_with_posting**(targets: list[[DataStoreRatingTarget](#datastoreratingtarget)], rate_param: list[[DataStoreRateObjectParam](#datastorerateobjectparam)], post_param: list[[DataStorePreparePostParam](#datastorepreparepostparam)], transactional: bool, fetch_ratings: bool) -> [RMCResponse](common.md)</code><br>
<span class="docs">Calls method `44` on the server. The RMC response has the following attributes:<br>
<span class="docs">
<code>ratings: list[[DataStoreRatingInfo](#datastoreratinginfo)]</code><br>
<code>results: list[[Result](common.md#result)]</code><br>
</span>
</span>

<code>**async def get_object_infos**(data_ids: list[int]) -> [RMCResponse](common.md)</code><br>
<span class="docs">Calls method `45` on the server. The RMC response has the following attributes:<br>
<span class="docs">
<code>infos: list[[DataStoreReqGetInfo](#datastorereqgetinfo)]</code><br>
<code>results: list[[Result](common.md#result)]</code><br>
</span>
</span>

<code>**async def search_object_light**(param: [DataStoreSearchParam](#datastoresearchparam)) -> [DataStoreSearchResult](#datastoresearchresult)</code><br>
<span class="docs">Calls method `46` on the server.</span>

<code>**async def coconut_register_meta**(meta: [CoconutMeta](#coconutmeta), url: str) -> None</code><br>
<span class="docs">Calls method `47` on the server.</span>

<code>**async def coconut_rate_post**(data_id: int) -> None</code><br>
<span class="docs">Calls method `48` on the server.</span>

<code>**async def coconut_get_object_infos**(param: [CoconutGetParam](#coconutgetparam)) -> [RMCResponse](common.md)</code><br>
<span class="docs">Calls method `49` on the server. The RMC response has the following attributes:<br>
<span class="docs">
<code>p_infos: list[[CoconutGetInfo](#coconutgetinfo)]</code><br>
<code>p_results: list[[Result](common.md#result)]</code><br>
</span>
</span>

<code>**async def coconut_report_violation**(violation: [CoconutViolation](#coconutviolation)) -> None</code><br>
<span class="docs">Calls method `50` on the server.</span>

<code>**async def upload_regular_match_result**(stats: [CalicoRegularStats](#calicoregularstats)) -> None</code><br>
<span class="docs">Calls method `51` on the server.</span>

<code>**async def upload_gachi_match_result**(stats: [CalicoGachiStats](#calicogachistats)) -> None</code><br>
<span class="docs">Calls method `52` on the server.</span>

<code>**async def upload_league_match_result**(stats: [CalicoLeagueStats](#calicoleaguestats)) -> None</code><br>
<span class="docs">Calls method `53` on the server.</span>

<code>**async def upload_fes_match_result**(stats: [CalicoFesStats](#calicofesstats)) -> None</code><br>
<span class="docs">Calls method `54` on the server.</span>

<code>**async def get_ordered_gear**() -> [OrderedInfo](#orderedinfo)</code><br>
<span class="docs">Calls method `55` on the server.</span>

<code>**async def purchase_gear**(info: [OrderedInfo](#orderedinfo)) -> None</code><br>
<span class="docs">Calls method `56` on the server.</span>

<code>**async def upload_time_attack**(info: [TimeAttackInfo](#timeattackinfo)) -> None</code><br>
<span class="docs">Calls method `57` on the server.</span>

<code>**async def coconut_register_meta_by_param**(meta: [CoconutMeta](#coconutmeta), sns_name: str, post_id: str) -> None</code><br>
<span class="docs">Calls method `58` on the server.</span>

<code>**async def upload_fes_match_result_v2**(stats: [CalicoFesStatsV2](#calicofesstatsv2)) -> None</code><br>
<span class="docs">Calls method `59` on the server.</span>

<code>**async def upload_x_match_result**(stats: [CalicoXStats](#calicoxstats)) -> None</code><br>
<span class="docs">Calls method `60` on the server.</span>

<code>**async def prepare_post_play_log**(param: [PlayLogPreparePostParam](#playlogpreparepostparam)) -> [DataStoreReqPostInfo](#datastorereqpostinfo)</code><br>
<span class="docs">Calls method `66` on the server.</span>

<code>**async def prepare_get_play_log**(param: [PlayLogPrepareGetParam](#playlogpreparegetparam)) -> [DataStoreReqGetInfo](#datastorereqgetinfo)</code><br>
<span class="docs">Calls method `67` on the server.</span>

## DataStoreServerS2
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new [`DataStoreServerS2`](#datastoreservers2).</span>

<code>**async def logout**(client: [RMCClient](rmc.md#rmcclient)) -> None</code><br>
<span class="docs">Called whenever a client is disconnected. May be overridden by a subclass.</span>

<code>**async def prepare_get_object_v1**(client: [RMCClient](rmc.md#rmcclient), param: [DataStorePrepareGetParamV1](#datastorepreparegetparamv1)) -> [DataStoreReqGetInfoV1](#datastorereqgetinfov1)</code><br>
<span class="docs">Handler for method `1`. This method should be overridden by a subclass.</span>

<code>**async def prepare_post_object_v1**(client: [RMCClient](rmc.md#rmcclient), param: [DataStorePreparePostParamV1](#datastorepreparepostparamv1)) -> [DataStoreReqPostInfoV1](#datastorereqpostinfov1)</code><br>
<span class="docs">Handler for method `2`. This method should be overridden by a subclass.</span>

<code>**async def complete_post_object_v1**(client: [RMCClient](rmc.md#rmcclient), param: [DataStoreCompletePostParamV1](#datastorecompletepostparamv1)) -> None</code><br>
<span class="docs">Handler for method `3`. This method should be overridden by a subclass.</span>

<code>**async def delete_object**(client: [RMCClient](rmc.md#rmcclient), param: [DataStoreDeleteParam](#datastoredeleteparam)) -> None</code><br>
<span class="docs">Handler for method `4`. This method should be overridden by a subclass.</span>

<code>**async def delete_objects**(client: [RMCClient](rmc.md#rmcclient), param: list[[DataStoreDeleteParam](#datastoredeleteparam)], transactional: bool) -> list[[Result](common.md#result)]</code><br>
<span class="docs">Handler for method `5`. This method should be overridden by a subclass.</span>

<code>**async def change_meta_v1**(client: [RMCClient](rmc.md#rmcclient), param: [DataStoreChangeMetaParamV1](#datastorechangemetaparamv1)) -> None</code><br>
<span class="docs">Handler for method `6`. This method should be overridden by a subclass.</span>

<code>**async def change_metas_v1**(client: [RMCClient](rmc.md#rmcclient), data_ids: list[int], param: list[[DataStoreChangeMetaParamV1](#datastorechangemetaparamv1)], transactional: bool) -> list[[Result](common.md#result)]</code><br>
<span class="docs">Handler for method `7`. This method should be overridden by a subclass.</span>

<code>**async def get_meta**(client: [RMCClient](rmc.md#rmcclient), param: [DataStoreGetMetaParam](#datastoregetmetaparam)) -> [DataStoreMetaInfo](#datastoremetainfo)</code><br>
<span class="docs">Handler for method `8`. This method should be overridden by a subclass.</span>

<code>**async def get_metas**(client: [RMCClient](rmc.md#rmcclient), data_ids: list[int], param: [DataStoreGetMetaParam](#datastoregetmetaparam)) -> [RMCResponse](common.md)</code><br>
<span class="docs">Handler for method `9`. This method should be overridden by a subclass. The RMC response must have the following attributes:<br>
<span class="docs">
<code>info: list[[DataStoreMetaInfo](#datastoremetainfo)]</code><br>
<code>results: list[[Result](common.md#result)]</code><br>
</span>
</span>

<code>**async def prepare_update_object**(client: [RMCClient](rmc.md#rmcclient), param: [DataStorePrepareUpdateParam](#datastoreprepareupdateparam)) -> [DataStoreReqUpdateInfo](#datastorerequpdateinfo)</code><br>
<span class="docs">Handler for method `10`. This method should be overridden by a subclass.</span>

<code>**async def complete_update_object**(client: [RMCClient](rmc.md#rmcclient), param: [DataStoreCompleteUpdateParam](#datastorecompleteupdateparam)) -> None</code><br>
<span class="docs">Handler for method `11`. This method should be overridden by a subclass.</span>

<code>**async def search_object**(client: [RMCClient](rmc.md#rmcclient), param: [DataStoreSearchParam](#datastoresearchparam)) -> [DataStoreSearchResult](#datastoresearchresult)</code><br>
<span class="docs">Handler for method `12`. This method should be overridden by a subclass.</span>

<code>**async def get_notification_url**(client: [RMCClient](rmc.md#rmcclient), param: [DataStoreGetNotificationUrlParam](#datastoregetnotificationurlparam)) -> [DataStoreReqGetNotificationUrlInfo](#datastorereqgetnotificationurlinfo)</code><br>
<span class="docs">Handler for method `13`. This method should be overridden by a subclass.</span>

<code>**async def get_new_arrived_notifications_v1**(client: [RMCClient](rmc.md#rmcclient), param: [DataStoreGetNewArrivedNotificationsParam](#datastoregetnewarrivednotificationsparam)) -> [RMCResponse](common.md)</code><br>
<span class="docs">Handler for method `14`. This method should be overridden by a subclass. The RMC response must have the following attributes:<br>
<span class="docs">
<code>result: list[[DataStoreNotificationV1](#datastorenotificationv1)]</code><br>
<code>has_next: bool</code><br>
</span>
</span>

<code>**async def rate_object**(client: [RMCClient](rmc.md#rmcclient), target: [DataStoreRatingTarget](#datastoreratingtarget), param: [DataStoreRateObjectParam](#datastorerateobjectparam), fetch_ratings: bool) -> [DataStoreRatingInfo](#datastoreratinginfo)</code><br>
<span class="docs">Handler for method `15`. This method should be overridden by a subclass.</span>

<code>**async def get_rating**(client: [RMCClient](rmc.md#rmcclient), target: [DataStoreRatingTarget](#datastoreratingtarget), access_password: int) -> [DataStoreRatingInfo](#datastoreratinginfo)</code><br>
<span class="docs">Handler for method `16`. This method should be overridden by a subclass.</span>

<code>**async def get_ratings**(client: [RMCClient](rmc.md#rmcclient), data_ids: list[int], access_password: int) -> [RMCResponse](common.md)</code><br>
<span class="docs">Handler for method `17`. This method should be overridden by a subclass. The RMC response must have the following attributes:<br>
<span class="docs">
<code>ratings: list[list[[DataStoreRatingInfoWithSlot](#datastoreratinginfowithslot)]]</code><br>
<code>results: list[[Result](common.md#result)]</code><br>
</span>
</span>

<code>**async def reset_rating**(client: [RMCClient](rmc.md#rmcclient), target: [DataStoreRatingTarget](#datastoreratingtarget), update_password: int) -> None</code><br>
<span class="docs">Handler for method `18`. This method should be overridden by a subclass.</span>

<code>**async def reset_ratings**(client: [RMCClient](rmc.md#rmcclient), data_ids: list[int], transactional: bool) -> list[[Result](common.md#result)]</code><br>
<span class="docs">Handler for method `19`. This method should be overridden by a subclass.</span>

<code>**async def get_specific_meta_v1**(client: [RMCClient](rmc.md#rmcclient), param: [DataStoreGetSpecificMetaParamV1](#datastoregetspecificmetaparamv1)) -> list[[DataStoreSpecificMetaInfoV1](#datastorespecificmetainfov1)]</code><br>
<span class="docs">Handler for method `20`. This method should be overridden by a subclass.</span>

<code>**async def post_meta_binary**(client: [RMCClient](rmc.md#rmcclient), param: [DataStorePreparePostParam](#datastorepreparepostparam)) -> int</code><br>
<span class="docs">Handler for method `21`. This method should be overridden by a subclass.</span>

<code>**async def touch_object**(client: [RMCClient](rmc.md#rmcclient), param: [DataStoreTouchObjectParam](#datastoretouchobjectparam)) -> None</code><br>
<span class="docs">Handler for method `22`. This method should be overridden by a subclass.</span>

<code>**async def get_rating_with_log**(client: [RMCClient](rmc.md#rmcclient), target: [DataStoreRatingTarget](#datastoreratingtarget), access_password: int) -> [RMCResponse](common.md)</code><br>
<span class="docs">Handler for method `23`. This method should be overridden by a subclass. The RMC response must have the following attributes:<br>
<span class="docs">
<code>rating: [DataStoreRatingInfo](#datastoreratinginfo)</code><br>
<code>log: [DataStoreRatingLog](#datastoreratinglog)</code><br>
</span>
</span>

<code>**async def prepare_post_object**(client: [RMCClient](rmc.md#rmcclient), param: [DataStorePreparePostParam](#datastorepreparepostparam)) -> [DataStoreReqPostInfo](#datastorereqpostinfo)</code><br>
<span class="docs">Handler for method `24`. This method should be overridden by a subclass.</span>

<code>**async def prepare_get_object**(client: [RMCClient](rmc.md#rmcclient), param: [DataStorePrepareGetParam](#datastorepreparegetparam)) -> [DataStoreReqGetInfo](#datastorereqgetinfo)</code><br>
<span class="docs">Handler for method `25`. This method should be overridden by a subclass.</span>

<code>**async def complete_post_object**(client: [RMCClient](rmc.md#rmcclient), param: [DataStoreCompletePostParam](#datastorecompletepostparam)) -> None</code><br>
<span class="docs">Handler for method `26`. This method should be overridden by a subclass.</span>

<code>**async def get_new_arrived_notifications**(client: [RMCClient](rmc.md#rmcclient), param: [DataStoreGetNewArrivedNotificationsParam](#datastoregetnewarrivednotificationsparam)) -> [RMCResponse](common.md)</code><br>
<span class="docs">Handler for method `27`. This method should be overridden by a subclass. The RMC response must have the following attributes:<br>
<span class="docs">
<code>result: list[[DataStoreNotification](#datastorenotification)]</code><br>
<code>has_next: bool</code><br>
</span>
</span>

<code>**async def get_specific_meta**(client: [RMCClient](rmc.md#rmcclient), param: [DataStoreGetSpecificMetaParam](#datastoregetspecificmetaparam)) -> list[[DataStoreSpecificMetaInfo](#datastorespecificmetainfo)]</code><br>
<span class="docs">Handler for method `28`. This method should be overridden by a subclass.</span>

<code>**async def get_persistence_info**(client: [RMCClient](rmc.md#rmcclient), owner_id: int, slot_id: int) -> [DataStorePersistenceInfo](#datastorepersistenceinfo)</code><br>
<span class="docs">Handler for method `29`. This method should be overridden by a subclass.</span>

<code>**async def get_persistence_infos**(client: [RMCClient](rmc.md#rmcclient), owner_id: int, slot_ids: list[int]) -> [RMCResponse](common.md)</code><br>
<span class="docs">Handler for method `30`. This method should be overridden by a subclass. The RMC response must have the following attributes:<br>
<span class="docs">
<code>infos: list[[DataStorePersistenceInfo](#datastorepersistenceinfo)]</code><br>
<code>results: list[[Result](common.md#result)]</code><br>
</span>
</span>

<code>**async def perpetuate_object**(client: [RMCClient](rmc.md#rmcclient), persistence_slot_id: int, data_id: int, delete_last_object: bool) -> None</code><br>
<span class="docs">Handler for method `31`. This method should be overridden by a subclass.</span>

<code>**async def unperpetuate_object**(client: [RMCClient](rmc.md#rmcclient), persistence_slot_id: int, delete_last_object: bool) -> None</code><br>
<span class="docs">Handler for method `32`. This method should be overridden by a subclass.</span>

<code>**async def prepare_get_object_or_meta_binary**(client: [RMCClient](rmc.md#rmcclient), param: [DataStorePrepareGetParam](#datastorepreparegetparam)) -> [RMCResponse](common.md)</code><br>
<span class="docs">Handler for method `33`. This method should be overridden by a subclass. The RMC response must have the following attributes:<br>
<span class="docs">
<code>get_info: [DataStoreReqGetInfo](#datastorereqgetinfo)</code><br>
<code>additional_meta: [DataStoreReqGetAdditionalMeta](#datastorereqgetadditionalmeta)</code><br>
</span>
</span>

<code>**async def get_password_info**(client: [RMCClient](rmc.md#rmcclient), data_id: int) -> [DataStorePasswordInfo](#datastorepasswordinfo)</code><br>
<span class="docs">Handler for method `34`. This method should be overridden by a subclass.</span>

<code>**async def get_password_infos**(client: [RMCClient](rmc.md#rmcclient), data_ids: list[int]) -> [RMCResponse](common.md)</code><br>
<span class="docs">Handler for method `35`. This method should be overridden by a subclass. The RMC response must have the following attributes:<br>
<span class="docs">
<code>infos: list[[DataStorePasswordInfo](#datastorepasswordinfo)]</code><br>
<code>results: list[[Result](common.md#result)]</code><br>
</span>
</span>

<code>**async def get_metas_multiple_param**(client: [RMCClient](rmc.md#rmcclient), params: list[[DataStoreGetMetaParam](#datastoregetmetaparam)]) -> [RMCResponse](common.md)</code><br>
<span class="docs">Handler for method `36`. This method should be overridden by a subclass. The RMC response must have the following attributes:<br>
<span class="docs">
<code>infos: list[[DataStoreMetaInfo](#datastoremetainfo)]</code><br>
<code>results: list[[Result](common.md#result)]</code><br>
</span>
</span>

<code>**async def complete_post_objects**(client: [RMCClient](rmc.md#rmcclient), data_ids: list[int]) -> None</code><br>
<span class="docs">Handler for method `37`. This method should be overridden by a subclass.</span>

<code>**async def change_meta**(client: [RMCClient](rmc.md#rmcclient), param: [DataStoreChangeMetaParam](#datastorechangemetaparam)) -> None</code><br>
<span class="docs">Handler for method `38`. This method should be overridden by a subclass.</span>

<code>**async def change_metas**(client: [RMCClient](rmc.md#rmcclient), data_ids: list[int], param: list[[DataStoreChangeMetaParam](#datastorechangemetaparam)], transactional: bool) -> list[[Result](common.md#result)]</code><br>
<span class="docs">Handler for method `39`. This method should be overridden by a subclass.</span>

<code>**async def rate_objects**(client: [RMCClient](rmc.md#rmcclient), targets: list[[DataStoreRatingTarget](#datastoreratingtarget)], param: list[[DataStoreRateObjectParam](#datastorerateobjectparam)], transactional: bool, fetch_ratings: bool) -> [RMCResponse](common.md)</code><br>
<span class="docs">Handler for method `40`. This method should be overridden by a subclass. The RMC response must have the following attributes:<br>
<span class="docs">
<code>infos: list[[DataStoreRatingInfo](#datastoreratinginfo)]</code><br>
<code>results: list[[Result](common.md#result)]</code><br>
</span>
</span>

<code>**async def post_meta_binary_with_data_id**(client: [RMCClient](rmc.md#rmcclient), data_id: int, param: [DataStorePreparePostParam](#datastorepreparepostparam)) -> None</code><br>
<span class="docs">Handler for method `41`. This method should be overridden by a subclass.</span>

<code>**async def post_meta_binaries_with_data_id**(client: [RMCClient](rmc.md#rmcclient), data_ids: list[int], param: list[[DataStorePreparePostParam](#datastorepreparepostparam)], transactional: bool) -> list[[Result](common.md#result)]</code><br>
<span class="docs">Handler for method `42`. This method should be overridden by a subclass.</span>

<code>**async def rate_object_with_posting**(client: [RMCClient](rmc.md#rmcclient), target: [DataStoreRatingTarget](#datastoreratingtarget), rate_param: [DataStoreRateObjectParam](#datastorerateobjectparam), post_param: [DataStorePreparePostParam](#datastorepreparepostparam), fetch_ratings: bool) -> [DataStoreRatingInfo](#datastoreratinginfo)</code><br>
<span class="docs">Handler for method `43`. This method should be overridden by a subclass.</span>

<code>**async def rate_objects_with_posting**(client: [RMCClient](rmc.md#rmcclient), targets: list[[DataStoreRatingTarget](#datastoreratingtarget)], rate_param: list[[DataStoreRateObjectParam](#datastorerateobjectparam)], post_param: list[[DataStorePreparePostParam](#datastorepreparepostparam)], transactional: bool, fetch_ratings: bool) -> [RMCResponse](common.md)</code><br>
<span class="docs">Handler for method `44`. This method should be overridden by a subclass. The RMC response must have the following attributes:<br>
<span class="docs">
<code>ratings: list[[DataStoreRatingInfo](#datastoreratinginfo)]</code><br>
<code>results: list[[Result](common.md#result)]</code><br>
</span>
</span>

<code>**async def get_object_infos**(client: [RMCClient](rmc.md#rmcclient), data_ids: list[int]) -> [RMCResponse](common.md)</code><br>
<span class="docs">Handler for method `45`. This method should be overridden by a subclass. The RMC response must have the following attributes:<br>
<span class="docs">
<code>infos: list[[DataStoreReqGetInfo](#datastorereqgetinfo)]</code><br>
<code>results: list[[Result](common.md#result)]</code><br>
</span>
</span>

<code>**async def search_object_light**(client: [RMCClient](rmc.md#rmcclient), param: [DataStoreSearchParam](#datastoresearchparam)) -> [DataStoreSearchResult](#datastoresearchresult)</code><br>
<span class="docs">Handler for method `46`. This method should be overridden by a subclass.</span>

<code>**async def coconut_register_meta**(client: [RMCClient](rmc.md#rmcclient), meta: [CoconutMeta](#coconutmeta), url: str) -> None</code><br>
<span class="docs">Handler for method `47`. This method should be overridden by a subclass.</span>

<code>**async def coconut_rate_post**(client: [RMCClient](rmc.md#rmcclient), data_id: int) -> None</code><br>
<span class="docs">Handler for method `48`. This method should be overridden by a subclass.</span>

<code>**async def coconut_get_object_infos**(client: [RMCClient](rmc.md#rmcclient), param: [CoconutGetParam](#coconutgetparam)) -> [RMCResponse](common.md)</code><br>
<span class="docs">Handler for method `49`. This method should be overridden by a subclass. The RMC response must have the following attributes:<br>
<span class="docs">
<code>p_infos: list[[CoconutGetInfo](#coconutgetinfo)]</code><br>
<code>p_results: list[[Result](common.md#result)]</code><br>
</span>
</span>

<code>**async def coconut_report_violation**(client: [RMCClient](rmc.md#rmcclient), violation: [CoconutViolation](#coconutviolation)) -> None</code><br>
<span class="docs">Handler for method `50`. This method should be overridden by a subclass.</span>

<code>**async def upload_regular_match_result**(client: [RMCClient](rmc.md#rmcclient), stats: [CalicoRegularStats](#calicoregularstats)) -> None</code><br>
<span class="docs">Handler for method `51`. This method should be overridden by a subclass.</span>

<code>**async def upload_gachi_match_result**(client: [RMCClient](rmc.md#rmcclient), stats: [CalicoGachiStats](#calicogachistats)) -> None</code><br>
<span class="docs">Handler for method `52`. This method should be overridden by a subclass.</span>

<code>**async def upload_league_match_result**(client: [RMCClient](rmc.md#rmcclient), stats: [CalicoLeagueStats](#calicoleaguestats)) -> None</code><br>
<span class="docs">Handler for method `53`. This method should be overridden by a subclass.</span>

<code>**async def upload_fes_match_result**(client: [RMCClient](rmc.md#rmcclient), stats: [CalicoFesStats](#calicofesstats)) -> None</code><br>
<span class="docs">Handler for method `54`. This method should be overridden by a subclass.</span>

<code>**async def get_ordered_gear**(client: [RMCClient](rmc.md#rmcclient)) -> [OrderedInfo](#orderedinfo)</code><br>
<span class="docs">Handler for method `55`. This method should be overridden by a subclass.</span>

<code>**async def purchase_gear**(client: [RMCClient](rmc.md#rmcclient), info: [OrderedInfo](#orderedinfo)) -> None</code><br>
<span class="docs">Handler for method `56`. This method should be overridden by a subclass.</span>

<code>**async def upload_time_attack**(client: [RMCClient](rmc.md#rmcclient), info: [TimeAttackInfo](#timeattackinfo)) -> None</code><br>
<span class="docs">Handler for method `57`. This method should be overridden by a subclass.</span>

<code>**async def coconut_register_meta_by_param**(client: [RMCClient](rmc.md#rmcclient), meta: [CoconutMeta](#coconutmeta), sns_name: str, post_id: str) -> None</code><br>
<span class="docs">Handler for method `58`. This method should be overridden by a subclass.</span>

<code>**async def upload_fes_match_result_v2**(client: [RMCClient](rmc.md#rmcclient), stats: [CalicoFesStatsV2](#calicofesstatsv2)) -> None</code><br>
<span class="docs">Handler for method `59`. This method should be overridden by a subclass.</span>

<code>**async def upload_x_match_result**(client: [RMCClient](rmc.md#rmcclient), stats: [CalicoXStats](#calicoxstats)) -> None</code><br>
<span class="docs">Handler for method `60`. This method should be overridden by a subclass.</span>

<code>**async def prepare_post_play_log**(client: [RMCClient](rmc.md#rmcclient), param: [PlayLogPreparePostParam](#playlogpreparepostparam)) -> [DataStoreReqPostInfo](#datastorereqpostinfo)</code><br>
<span class="docs">Handler for method `66`. This method should be overridden by a subclass.</span>

<code>**async def prepare_get_play_log**(client: [RMCClient](rmc.md#rmcclient), param: [PlayLogPrepareGetParam](#playlogpreparegetparam)) -> [DataStoreReqGetInfo](#datastorereqgetinfo)</code><br>
<span class="docs">Handler for method `67`. This method should be overridden by a subclass.</span>

## CalicoFesStats
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `CalicoFesStats` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>fes_id: int</code><br>
<code>theme_id: int</code><br>
<code>fes_grade: int</code><br>
<code>fes_point: int</code><br>
<code>fes_power: int</code><br>
<code>max_fes_power: int</code><br>
<code>my_estimate_fes_power: int</code><br>
<code>other_estimate_fes_power: int</code><br>
</span><br>

## CalicoFesStatsV2
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `CalicoFesStatsV2` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>other_theme_id: int</code><br>
</span><br>

## CalicoGachiStats
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `CalicoGachiStats` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>elapsed_time: int</code><br>
<code>my_team_count: int</code><br>
<code>other_team_count: int</code><br>
<code>udemae: int</code><br>
<code>estimate_gachi_power: int</code><br>
</span><br>

## CalicoLeagueStats
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `CalicoLeagueStats` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>league_id: str</code><br>
<code>tag_id: int</code><br>
<code>league_point: int</code><br>
<code>max_league_point: int</code><br>
<code>my_estimate_league_point: int</code><br>
<code>other_estimate_league_point: int</code><br>
</span><br>

## CalicoPlayerResult
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `CalicoPlayerResult` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>player_simple: [CalicoPlayerSimple](#calicoplayersimple) = [CalicoPlayerSimple](#calicoplayersimple)()</code><br>
<code>kill_count: int</code><br>
<code>assist_count: int</code><br>
<code>death_count: int</code><br>
<code>special_count: int</code><br>
<code>game_paint_point: int</code><br>
<code>sort_score: int</code><br>
</span><br>

## CalicoPlayerSimple
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `CalicoPlayerSimple` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>pid: int</code><br>
<code>name: str</code><br>
<code>player_type: int</code><br>
<code>udemae: int</code><br>
<code>player_rank: int</code><br>
<code>star_rank: int</code><br>
<code>fes_grade: int</code><br>
<code>weapon_id: int</code><br>
<code>head_id: int</code><br>
<code>head_skill_ids: list[int]</code><br>
<code>clothes_ids: int</code><br>
<code>clothes_skill_ids: list[int]</code><br>
<code>shoes_id: int</code><br>
<code>shoes_skill_ids: list[int]</code><br>
</span><br>

## CalicoRegularStats
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `CalicoRegularStats` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>my_team_percentage: int</code><br>
<code>other_team_percentage: int</code><br>
<code>win_meter: int</code><br>
</span><br>

## CalicoStatsBase
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `CalicoStatsBase` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>game_mode: int</code><br>
<code>rule: int</code><br>
<code>result: int</code><br>
<code>stage: int</code><br>
<code>player_result: [CalicoPlayerResult](#calicoplayerresult) = [CalicoPlayerResult](#calicoplayerresult)()</code><br>
<code>my_team_members: list[[CalicoPlayerResult](#calicoplayerresult)]</code><br>
<code>other_team_members: list[[CalicoPlayerResult](#calicoplayerresult)]</code><br>
<code>weapon_paint_point: int</code><br>
<code>start_time: [DateTime](common.md#datetime)</code><br>
<code>battle_num: int</code><br>
<code>player_rank: int</code><br>
<code>star_rank: int</code><br>
</span><br>

## CalicoXStats
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `CalicoXStats` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>crown_players: list[int]</code><br>
<code>estimate_x_power: int</code><br>
<code>x_power: int</code><br>
<code>rank: int</code><br>
</span><br>

## CoconutGetInfo
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `CoconutGetInfo` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>info: [DataStoreReqGetInfo](#datastorereqgetinfo) = [DataStoreReqGetInfo](#datastorereqgetinfo)()</code><br>
<code>meta: [CoconutMeta](#coconutmeta) = [CoconutMeta](#coconutmeta)()</code><br>
</span><br>

## CoconutGetParam
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `CoconutGetParam` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>unique_ids: list[int]</code><br>
<code>get_type: int</code><br>
<code>region: int</code><br>
<code>festival_id: int</code><br>
</span><br>

## CoconutMeta
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `CoconutMeta` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>data_id: int</code><br>
<code>tweet_id: int</code><br>
<code>region: int</code><br>
<code>post_type: int</code><br>
<code>theme_id: int</code><br>
<code>festival_id: int</code><br>
<code>language: str</code><br>
<code>binary_data: bytes</code><br>
</span><br>

## CoconutViolation
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `CoconutViolation` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>data_id: int</code><br>
<code>category_code: str</code><br>
<code>reason: str</code><br>
</span><br>

## DataStoreChangeMetaCompareParam
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStoreChangeMetaCompareParam` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>comparison_flag: int</code><br>
<code>name: str</code><br>
<code>permission: [DataStorePermission](#datastorepermission) = [DataStorePermission](#datastorepermission)()</code><br>
<code>delete_permission: [DataStorePermission](#datastorepermission) = [DataStorePermission](#datastorepermission)()</code><br>
<code>period: int</code><br>
<code>meta_binary: bytes</code><br>
<code>tags: list[str]</code><br>
<code>referred_count: int</code><br>
<code>data_type: int</code><br>
<code>status: int</code><br>
</span><br>

## DataStoreChangeMetaParam
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStoreChangeMetaParam` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>data_id: int</code><br>
<code>modifies_flag: int</code><br>
<code>name: str</code><br>
<code>permission: [DataStorePermission](#datastorepermission) = [DataStorePermission](#datastorepermission)()</code><br>
<code>delete_permission: [DataStorePermission](#datastorepermission) = [DataStorePermission](#datastorepermission)()</code><br>
<code>period: int</code><br>
<code>meta_binary: bytes</code><br>
<code>tags: list[str]</code><br>
<code>update_password: int</code><br>
<code>referred_count: int</code><br>
<code>data_type: int</code><br>
<code>status: int</code><br>
<code>compare_param: [DataStoreChangeMetaCompareParam](#datastorechangemetacompareparam) = [DataStoreChangeMetaCompareParam](#datastorechangemetacompareparam)()</code><br>
<code>persistence_target: [DataStorePersistenceTarget](#datastorepersistencetarget) = [DataStorePersistenceTarget](#datastorepersistencetarget)()</code><br>
</span><br>

## DataStoreChangeMetaParamV1
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStoreChangeMetaParamV1` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>data_id: int</code><br>
<code>modifies_flag: int</code><br>
<code>name: str</code><br>
<code>permission: [DataStorePermission](#datastorepermission) = [DataStorePermission](#datastorepermission)()</code><br>
<code>delete_permission: [DataStorePermission](#datastorepermission) = [DataStorePermission](#datastorepermission)()</code><br>
<code>period: int</code><br>
<code>meta_binary: bytes</code><br>
<code>tags: list[str]</code><br>
<code>update_password: int</code><br>
</span><br>

## DataStoreCompletePostParam
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStoreCompletePostParam` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>data_id: int</code><br>
<code>success: bool</code><br>
</span><br>

## DataStoreCompletePostParamV1
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStoreCompletePostParamV1` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>data_id: int</code><br>
<code>success: bool</code><br>
</span><br>

## DataStoreCompleteUpdateParam
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStoreCompleteUpdateParam` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>data_id: int</code><br>
<code>version: int</code><br>
<code>success: bool</code><br>
</span><br>

## DataStoreDeleteParam
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStoreDeleteParam` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>data_id: int</code><br>
<code>update_password: int</code><br>
</span><br>

## DataStoreGetMetaParam
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStoreGetMetaParam` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>data_id: int = 0</code><br>
<code>persistence_target: [DataStorePersistenceTarget](#datastorepersistencetarget) = [DataStorePersistenceTarget](#datastorepersistencetarget)()</code><br>
<code>result_option: int = 0</code><br>
<code>access_password: int = 0</code><br>
</span><br>

## DataStoreGetNewArrivedNotificationsParam
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStoreGetNewArrivedNotificationsParam` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>last_notification_id: int</code><br>
<code>limit: int</code><br>
</span><br>

## DataStoreGetNotificationUrlParam
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStoreGetNotificationUrlParam` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>previous_url: str</code><br>
</span><br>

## DataStoreGetSpecificMetaParam
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStoreGetSpecificMetaParam` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>data_ids: list[int]</code><br>
</span><br>

## DataStoreGetSpecificMetaParamV1
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStoreGetSpecificMetaParamV1` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>data_ids: list[int]</code><br>
</span><br>

## DataStoreKeyValue
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStoreKeyValue` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>key: str</code><br>
<code>value: str</code><br>
</span><br>

## DataStoreMetaInfo
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStoreMetaInfo` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>data_id: int</code><br>
<code>owner_id: int</code><br>
<code>size: int</code><br>
<code>name: str</code><br>
<code>data_type: int</code><br>
<code>meta_binary: bytes</code><br>
<code>permission: [DataStorePermission](#datastorepermission) = [DataStorePermission](#datastorepermission)()</code><br>
<code>delete_permission: [DataStorePermission](#datastorepermission) = [DataStorePermission](#datastorepermission)()</code><br>
<code>create_time: [DateTime](common.md#datetime)</code><br>
<code>update_time: [DateTime](common.md#datetime)</code><br>
<code>period: int</code><br>
<code>status: int</code><br>
<code>referred_count: int</code><br>
<code>refer_data_id: int</code><br>
<code>flag: int</code><br>
<code>referred_time: [DateTime](common.md#datetime)</code><br>
<code>expire_time: [DateTime](common.md#datetime)</code><br>
<code>tags: list[str]</code><br>
<code>ratings: list[[DataStoreRatingInfoWithSlot](#datastoreratinginfowithslot)]</code><br>
</span><br>

## DataStoreNotification
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStoreNotification` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>notification_id: int</code><br>
<code>data_id: int</code><br>
</span><br>

## DataStoreNotificationV1
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStoreNotificationV1` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>notification_id: int</code><br>
<code>data_id: int</code><br>
</span><br>

## DataStorePasswordInfo
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStorePasswordInfo` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>data_id: int</code><br>
<code>access_password: int</code><br>
<code>update_password: int</code><br>
</span><br>

## DataStorePermission
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStorePermission` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>permission: int = 3</code><br>
<code>recipients: list[int] = []</code><br>
</span><br>

## DataStorePersistenceInfo
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStorePersistenceInfo` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>owner_id: int</code><br>
<code>slot_id: int</code><br>
<code>data_id: int</code><br>
</span><br>

## DataStorePersistenceInitParam
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStorePersistenceInitParam` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>persistence_id: int = 65535</code><br>
<code>delete_last_object: bool = True</code><br>
</span><br>

## DataStorePersistenceTarget
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStorePersistenceTarget` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>owner_id: int = 0</code><br>
<code>persistence_id: int = 65535</code><br>
</span><br>

## DataStorePrepareGetParam
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStorePrepareGetParam` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>data_id: int = 0</code><br>
<code>lock_id: int = 0</code><br>
<code>persistence_target: [DataStorePersistenceTarget](#datastorepersistencetarget) = [DataStorePersistenceTarget](#datastorepersistencetarget)()</code><br>
<code>access_password: int = 0</code><br>
If `nex.version` >= 30500:<br>
<span class="docs">
<code>extra_data: list[str] = []</code><br>
</span><br>
</span><br>

## DataStorePrepareGetParamV1
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStorePrepareGetParamV1` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>data_id: int</code><br>
<code>lock_id: int = 0</code><br>
</span><br>

## DataStorePreparePostParam
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStorePreparePostParam` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>size: int</code><br>
<code>name: str</code><br>
<code>data_type: int</code><br>
<code>meta_binary: bytes</code><br>
<code>permission: [DataStorePermission](#datastorepermission) = [DataStorePermission](#datastorepermission)()</code><br>
<code>delete_permission: [DataStorePermission](#datastorepermission) = [DataStorePermission](#datastorepermission)()</code><br>
<code>flag: int</code><br>
<code>period: int</code><br>
<code>refer_data_id: int = 0</code><br>
<code>tags: list[str] = []</code><br>
<code>rating_init_param: list[[DataStoreRatingInitParamWithSlot](#datastoreratinginitparamwithslot)] = []</code><br>
<code>persistence_init_param: [DataStorePersistenceInitParam](#datastorepersistenceinitparam) = [DataStorePersistenceInitParam](#datastorepersistenceinitparam)()</code><br>
If `nex.version` >= 30500:<br>
<span class="docs">
<code>extra_data: list[str]</code><br>
</span><br>
</span><br>

## DataStorePreparePostParamV1
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStorePreparePostParamV1` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>size: int</code><br>
<code>name: str</code><br>
<code>data_type: int = 0</code><br>
<code>meta_binary: bytes = b""</code><br>
<code>permission: [DataStorePermission](#datastorepermission) = [DataStorePermission](#datastorepermission)()</code><br>
<code>delete_permission: [DataStorePermission](#datastorepermission) = [DataStorePermission](#datastorepermission)()</code><br>
<code>flag: int</code><br>
<code>period: int</code><br>
<code>refer_data_id: int = 0</code><br>
<code>tags: list[str]</code><br>
<code>rating_init_param: list[[DataStoreRatingInitParamWithSlot](#datastoreratinginitparamwithslot)]</code><br>
</span><br>

## DataStorePrepareUpdateParam
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStorePrepareUpdateParam` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>data_id: int</code><br>
<code>size: int</code><br>
<code>update_password: int</code><br>
<code>extra_data: list[str]</code><br>
</span><br>

## DataStoreRateObjectParam
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStoreRateObjectParam` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>rating_value: int</code><br>
<code>access_password: int</code><br>
</span><br>

## DataStoreRatingInfo
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStoreRatingInfo` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>total_value: int</code><br>
<code>count: int</code><br>
<code>initial_value: int</code><br>
</span><br>

## DataStoreRatingInfoWithSlot
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStoreRatingInfoWithSlot` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>slot: int</code><br>
<code>info: [DataStoreRatingInfo](#datastoreratinginfo) = [DataStoreRatingInfo](#datastoreratinginfo)()</code><br>
</span><br>

## DataStoreRatingInitParam
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStoreRatingInitParam` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>flag: int</code><br>
<code>internal_flag: int</code><br>
<code>lock_type: int</code><br>
<code>initial_value: int</code><br>
<code>range_min: int</code><br>
<code>range_max: int</code><br>
<code>period_hour: int</code><br>
<code>period_duration: int</code><br>
</span><br>

## DataStoreRatingInitParamWithSlot
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStoreRatingInitParamWithSlot` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>slot: int</code><br>
<code>param: [DataStoreRatingInitParam](#datastoreratinginitparam) = [DataStoreRatingInitParam](#datastoreratinginitparam)()</code><br>
</span><br>

## DataStoreRatingLog
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStoreRatingLog` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>is_rated: bool</code><br>
<code>pid: int</code><br>
<code>rating_value: int</code><br>
<code>lock_expiration_time: [DateTime](common.md#datetime)</code><br>
</span><br>

## DataStoreRatingTarget
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStoreRatingTarget` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>data_id: int</code><br>
<code>slot: int</code><br>
</span><br>

## DataStoreReqGetAdditionalMeta
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStoreReqGetAdditionalMeta` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>owner_id: int</code><br>
<code>data_type: int</code><br>
<code>version: int</code><br>
<code>meta_binary: bytes</code><br>
</span><br>

## DataStoreReqGetInfo
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStoreReqGetInfo` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>url: str</code><br>
<code>headers: list[[DataStoreKeyValue](#datastorekeyvalue)]</code><br>
<code>size: int</code><br>
<code>root_ca_cert: bytes</code><br>
If `nex.version` >= 30500:<br>
<span class="docs">
<code>data_id: int</code><br>
</span><br>
</span><br>

## DataStoreReqGetInfoV1
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStoreReqGetInfoV1` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>url: str</code><br>
<code>headers: list[[DataStoreKeyValue](#datastorekeyvalue)]</code><br>
<code>size: int</code><br>
<code>root_ca_cert: bytes</code><br>
</span><br>

## DataStoreReqGetNotificationUrlInfo
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStoreReqGetNotificationUrlInfo` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>url: str</code><br>
<code>key: str</code><br>
<code>query: str</code><br>
<code>root_ca_cert: bytes</code><br>
</span><br>

## DataStoreReqPostInfo
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStoreReqPostInfo` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>data_id: int</code><br>
<code>url: str</code><br>
<code>headers: list[[DataStoreKeyValue](#datastorekeyvalue)]</code><br>
<code>form: list[[DataStoreKeyValue](#datastorekeyvalue)]</code><br>
<code>root_ca_cert: bytes</code><br>
</span><br>

## DataStoreReqPostInfoV1
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStoreReqPostInfoV1` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>data_id: int</code><br>
<code>url: str</code><br>
<code>headers: list[[DataStoreKeyValue](#datastorekeyvalue)]</code><br>
<code>form: list[[DataStoreKeyValue](#datastorekeyvalue)]</code><br>
<code>root_ca_cert: bytes</code><br>
</span><br>

## DataStoreReqUpdateInfo
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStoreReqUpdateInfo` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>version: int</code><br>
<code>url: str</code><br>
<code>headers: list[[DataStoreKeyValue](#datastorekeyvalue)]</code><br>
<code>form: list[[DataStoreKeyValue](#datastorekeyvalue)]</code><br>
<code>root_ca_cert: bytes</code><br>
</span><br>

## DataStoreSearchParam
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStoreSearchParam` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>search_target: int = 1</code><br>
<code>owner_ids: list[int] = []</code><br>
<code>owner_type: int = 0</code><br>
<code>destination_ids: list[int] = []</code><br>
<code>data_type: int = 65535</code><br>
<code>created_after: [DateTime](common.md#datetime) = [DateTime](common.md#datetime).future()</code><br>
<code>created_before: [DateTime](common.md#datetime) = [DateTime](common.md#datetime).future()</code><br>
<code>updated_after: [DateTime](common.md#datetime) = [DateTime](common.md#datetime).future()</code><br>
<code>updated_before: [DateTime](common.md#datetime) = [DateTime](common.md#datetime).future()</code><br>
<code>refer_data_id: int = 0</code><br>
<code>tags: list[str] = []</code><br>
<code>result_order_column: int = 0</code><br>
<code>result_order: int = 0</code><br>
<code>result_range: [ResultRange](common.md#resultrange) = [ResultRange](common.md#resultrange)()</code><br>
<code>result_option: int = 0</code><br>
<code>minimal_rating_frequency: int = 0</code><br>
<code>use_cache: bool = False</code><br>
<code>total_count_enabled: bool = True</code><br>
<code>data_types: list[int] = []</code><br>
</span><br>

## DataStoreSearchResult
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStoreSearchResult` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>total_count: int</code><br>
<code>result: list[[DataStoreMetaInfo](#datastoremetainfo)]</code><br>
<code>total_count_type: int</code><br>
</span><br>

## DataStoreSpecificMetaInfo
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStoreSpecificMetaInfo` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>data_id: int</code><br>
<code>owner_id: int</code><br>
<code>size: int</code><br>
<code>data_type: int</code><br>
<code>version: int</code><br>
</span><br>

## DataStoreSpecificMetaInfoV1
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStoreSpecificMetaInfoV1` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>data_id: int</code><br>
<code>owner_id: int</code><br>
<code>size: int</code><br>
<code>data_type: int</code><br>
<code>version: int</code><br>
</span><br>

## DataStoreTouchObjectParam
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `DataStoreTouchObjectParam` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>data_id: int</code><br>
<code>lock_id: int</code><br>
<code>access_password: int</code><br>
</span><br>

## OrderedInfo
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `OrderedInfo` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>gear_kind: int</code><br>
<code>gear_id: int</code><br>
<code>skill_id: int</code><br>
<code>price: int</code><br>
</span><br>

## PlayLogEntry
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `PlayLogEntry` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>user_id: int</code><br>
<code>player_name: str</code><br>
<code>unknown: int</code><br>
<code>properties: dict[str, object]</code><br>
</span><br>

## PlayLogPrepareGetParam
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `PlayLogPrepareGetParam` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>unknown0: int</code><br>
<code>unknown1: [DateTime](common.md#datetime)</code><br>
<code>unknown2: int</code><br>
</span><br>

## PlayLogPreparePostParam
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `PlayLogPreparePostParam` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>entries: list[[PlayLogEntry](#playlogentry)]</code><br>
<code>play_time: [DateTime](common.md#datetime)</code><br>
<code>stage_id: int</code><br>
<code>unknown0: int</code><br>
<code>properties: dict[str, object]</code><br>
</span><br>

## StageTimeAttackInfo
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `StageTimeAttackInfo` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>clear_weapons: dict[int, [StageTimeAttackWeapon](#stagetimeattackweapon)]</code><br>
</span><br>

## StageTimeAttackWeapon
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `StageTimeAttackWeapon` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>weapon_level: int</code><br>
<code>clear_time: int</code><br>
</span><br>

## TimeAttackInfo
<code>**def _\_init__**()</code><br>
<span class="docs">Creates a new `TimeAttackInfo` instance. Required fields must be filled in manually.</span>

The following fields are defined in this class:<br>
<span class="docs">
<code>stage_infos: dict[int, [StageTimeAttackInfo](#stagetimeattackinfo)]</code><br>
</span><br>

