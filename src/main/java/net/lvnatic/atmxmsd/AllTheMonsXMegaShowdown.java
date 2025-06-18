package net.lvnatic.atmxmsd;

import net.fabricmc.api.ModInitializer;

import net.lvnatic.atmxmsd.item.ModItemGroups;
import net.lvnatic.atmxmsd.item.ModItems;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class AllTheMonsXMegaShowdown implements ModInitializer {
	public static final String MOD_ID = "atmxmsd";
	public static final Logger LOGGER = LoggerFactory.getLogger(MOD_ID);

	@Override
	public void onInitialize() {
		ModItemGroups.registerItemGroups();
		ModItems.registerModItems();
	}
}