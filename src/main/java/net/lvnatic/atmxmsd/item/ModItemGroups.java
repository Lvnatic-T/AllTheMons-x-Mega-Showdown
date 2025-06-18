package net.lvnatic.atmxmsd.item;

import net.fabricmc.fabric.api.itemgroup.v1.FabricItemGroup;
import net.lvnatic.atmxmsd.AllTheMonsXMegaShowdown;
import net.minecraft.item.ItemGroup;
import net.minecraft.item.ItemStack;
import net.minecraft.registry.Registries;
import net.minecraft.registry.Registry;
import net.minecraft.text.Text;
import net.minecraft.util.Identifier;

public class ModItemGroups {
    public static final ItemGroup ATMXMSD_ITEMS_GROUP = Registry.register(Registries.ITEM_GROUP,
            Identifier.of(AllTheMonsXMegaShowdown.MOD_ID, "atmxmsd_items"),
            FabricItemGroup.builder().icon(() -> new ItemStack(ModItems.BINDING_ARMOR))
                    .displayName(Text.translatable("itemgroup.atmxmsd.atmxmsd_items"))
                    .entries((displayContext, entries) -> {
                        entries.add(ModItems.BINDING_ARMOR);
                        entries.add(ModItems.SHADOW_ENERGY);
                        entries.add(ModItems.SHADOW_MEWTWONITE_Y);
                        entries.add(ModItems.SHADOW_MEWTWONITE_X);
                        entries.add(ModItems.ANCIENT_LIGHT_BALL);
                        entries.add(ModItems.COSTUME_BOX_INCINEROAR);
                        entries.add(ModItems.COSTUME_BOX_LUCARIO);
                        entries.add(ModItems.GREEN_SCARF);
                        entries.add(ModItems.RED_SCARF);
                        entries.add(ModItems.TIMEGEAR);
                        entries.add(ModItems.METEORITE);
                        entries.add(ModItems.WATER_SHURIKEN);
                        entries.add(ModItems.VICTINITE);

                    }).build());


    public static void registerItemGroups() {
        AllTheMonsXMegaShowdown.LOGGER.info("Registering Item Groups for " + AllTheMonsXMegaShowdown.MOD_ID);

    }
}
