import cx from 'clsx';
import { useState } from 'react';
import {
  Container,
  Avatar,
  UnstyledButton,
  Group,
  Text,
  Menu,
  Burger,
  rem,
  useMantineTheme,
  ActionIcon,
  useMantineColorScheme,
} from '@mantine/core';
import { useDisclosure } from '@mantine/hooks';
import {
  IconLogout,
  IconSettings,
  IconChevronDown,
  IconChecklist,
  IconSun,
  IconMoonStars,
} from '@tabler/icons-react';
import { useNavigate } from 'react-router-dom';
import classes from './Header.module.css';
import { useAuthProfileRetrieveQuery } from '@/redux/api';
import { useAppDispatch } from '@/redux/hooks';

export function Header() {
  const theme = useMantineTheme();
  const { data: profile } = useAuthProfileRetrieveQuery();
  const [opened, { toggle }] = useDisclosure(false);
  const [userMenuOpened, setUserMenuOpened] = useState(false);
  const { colorScheme, toggleColorScheme } = useMantineColorScheme();
  const dispatch = useAppDispatch();
  const navigate = useNavigate();
  const dark = colorScheme === 'dark';
  const sunIcon = (
    <IconSun
      style={{ width: rem(16), height: rem(16) }}
      stroke={2.5}
      color={theme.colors.yellow[4]}
    />
  );

  const moonIcon = (
    <IconMoonStars
      style={{ width: rem(16), height: rem(16) }}
      stroke={2.5}
      color={theme.colors.blue[6]}
    />
  );
  return (
    <div className={classes.header}>
      <Container className={classes.mainSection} size="md">
        <Group justify="space-between">
          <Burger opened={opened} onClick={toggle} hiddenFrom="xs" size="sm" />
          <IconChecklist />
          <Text>Remembrancer</Text>
          <Menu
            width={260}
            position="bottom-end"
            transitionProps={{ transition: 'pop-top-right' }}
            onClose={() => setUserMenuOpened(false)}
            onOpen={() => setUserMenuOpened(true)}
            withinPortal
          >
            <Menu.Target>
              <UnstyledButton
                className={cx(classes.user, { [classes.userActive]: userMenuOpened })}
              >
                <Group gap={7}>
                  <Avatar alt={profile?.first_name} radius="xl" size={20}>
                    {profile?.first_name.toUpperCase().charAt(0)}
                    {profile?.last_name.toUpperCase().charAt(0)}
                  </Avatar>
                  <Text fw={500} size="sm" lh={1} mr={3}>
                    {profile?.first_name} {profile?.last_name}
                  </Text>
                  <IconChevronDown style={{ width: rem(12), height: rem(12) }} stroke={1.5} />
                </Group>
              </UnstyledButton>
            </Menu.Target>
            <ActionIcon
              variant="outline"
              color={dark ? 'yellow' : 'blue'}
              onClick={() => toggleColorScheme()}
              title="Toggle color scheme"
            >
              {dark ? sunIcon : moonIcon}
            </ActionIcon>
            <Menu.Dropdown>
              <Menu.Item
                onClick={() => navigate('/profile')}
                leftSection={
                  <IconSettings style={{ width: rem(16), height: rem(16) }} stroke={1.5} />
                }
              >
                Account settings
              </Menu.Item>
              <Menu.Item
                onClick={() => dispatch({ type: 'auth/logout' })}
                leftSection={
                  <IconLogout style={{ width: rem(16), height: rem(16) }} stroke={1.5} />
                }
              >
                Logout
              </Menu.Item>
            </Menu.Dropdown>
          </Menu>
        </Group>
      </Container>
    </div>
  );
}
