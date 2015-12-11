"""Neutron LBaaSv2 Driver"""
# Copyright 2014 F5 Networks Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import f5.oslbaasv2driver.drivers.plugin_driver as f5driver

from oslo_log import log as logging

from neutron_lbaas.drivers import driver_base

VERSION = "2.0.0"
LOG = logging.getLogger(__name__)


class F5PluginDriverV2(driver_base.LoadBalancerBaseDriver):

    def __init__(self, plugin, env=None):
        super(F5PluginDriverV2, self).__init__(plugin)

        self.load_balancer = LoadBalancerManager(self)
        self.listener = ListenerManager(self)
        self.pool = PoolManager(self)
        self.member = MemberManager(self)
        self.health_monitor = HealthMonitorManager(self)

        LOG.debug("F5PluginDriverV2: initializing, version=%s, impl=%s"
                  % (VERSION, f5driver.VERSION))
        if not env:
            env = 'default'
        driver_impl = f5driver.F5PluginDriverV2(
            self, self._core_plugin, env
        )
        self.impl = driver_impl


class LoadBalancerManager(driver_base.BaseLoadBalancerManager):

    def create(self, context, lb):
        self.driver.impl.lb_create(context, lb)

    def update(self, context, old_lb, lb):
        self.driver.impl.lb_update(context, old_lb, lb)

    def delete(self, context, lb):
        self.driver.impl.lb_delete(context, lb)

    def refresh(self, context, lb):
        self.driver.impl.lb_refresh(context, lb)

    def stats(self, context, lb):
        return self.driver.impl.lb_stats(context, lb)


class ListenerManager(driver_base.BaseListenerManager):

    def create(self, context, listener):
        self.driver.impl.listener_create(context, listener)

    def update(self, context, old_listener, listener):
        self.driver.impl.listener_update(context, old_listener, listener)

    def delete(self, context, listener):
        self.driver.impl.listener_delete(context, listener)


class PoolManager(driver_base.BasePoolManager):

    def create(self, context, pool):
        self.driver.impl.pool_create(context, pool)

    def update(self, context, old_pool, pool):
        self.driver.impl.pool_update(context, old_pool, pool)

    def delete(self, context, pool):
        self.driver.impl.pool_delete(context, pool)


class MemberManager(driver_base.BaseMemberManager):

    def create(self, context, member):
        self.driver.impl.member_create(context, member)

    def update(self, context, old_member, member):
        self.driver.impl.member_update(context, old_member, member)

    def delete(self, context, member):
        self.driver.impl.member_delete(context, member)


class HealthMonitorManager(driver_base.BaseHealthMonitorManager):

    def create(self, context, hm):
        self.driver.impl.healthmonitor_create(context, hm)

    def update(self, context, old_hm, hm):
        self.driver.impl.healthmonitor_update(context, old_hm, hm)

    def delete(self, context, hm):
        self.driver.impl.healthmonitor_.delete(context, hm)
