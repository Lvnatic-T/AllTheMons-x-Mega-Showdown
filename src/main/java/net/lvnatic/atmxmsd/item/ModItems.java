package net.lvnatic.atmxmsd.item;

import net.lvnatic.atmxmsd.AllTheMonsXMegaShowdown;
import net.minecraft.item.Item;
import net.minecraft.registry.Registries;
import net.minecraft.registry.Registry;
import net.minecraft.util.Identifier;

public class ModItems {
    public static final Item SHADOW_ENERGY = registerItem("shadow_energy", new Item(new Item.Settings()));
    public static final Item ANCIENT_LIGHT_BALL = registerItem("ancient_light_ball", new Item(new Item.Settings()));
    public static final Item BINDING_ARMOR = registerItem("binding_armor", new Item(new Item.Settings()));
    public static final Item COSTUME_BOX_INCINEROAR = registerItem("costume_box_incineroar", new Item(new Item.Settings()));
    public static final Item COSTUME_BOX_LUCARIO = registerItem("costume_box_lucario", new Item(new Item.Settings()));
    public static final Item GREEN_SCARF = registerItem("green_scarf", new Item(new Item.Settings()));
    public static final Item METEORITE = registerItem("meteorite", new Item(new Item.Settings()));
    public static final Item RED_SCARF = registerItem("red_scarf", new Item(new Item.Settings()));
    public static final Item SHADOW_MEWTWONITE_X = registerItem("shadow_mewtwonite_x", new Item(new Item.Settings()));
    public static final Item SHADOW_MEWTWONITE_Y = registerItem("shadow_mewtwonite_y", new Item(new Item.Settings()));
    public static final Item TIMEGEAR = registerItem("timegear", new Item(new Item.Settings()));
    public static final Item VICTINITE = registerItem("victinite", new Item(new Item.Settings()));
    public static final Item WATER_SHURIKEN = registerItem("water_shuriken", new Item(new Item.Settings()));

    private static Item registerItem(String name, Item item) {
        return Registry.register(Registries.ITEM, Identifier.of(AllTheMonsXMegaShowdown.MOD_ID, name), item);
    }

    public static void registerModItems() {
        AllTheMonsXMegaShowdown.LOGGER.info("Registering Mod Items for " + AllTheMonsXMegaShowdown.MOD_ID);

    }
}
