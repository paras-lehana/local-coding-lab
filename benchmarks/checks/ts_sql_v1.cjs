// Independent behavior checks. Execute only in the Linux grading sandbox.
'use strict';
const assert = require('node:assert/strict');
const { normalizeJobs } = require('/tmp/out/candidate.js');
const results = [];
function check(name, body) {
  try { body(); results.push({ name, passed: true }); }
  catch (error) { results.push({ name, passed: false, error: String(error) }); }
}
check('defaults, trimming, order and exact output shape', () => {
  assert.deepEqual(normalizeJobs([{id:' a '}, {id:'b', extra:42}]), [
    {id:'a', count:1, enabled:true, tags:[]},
    {id:'b', count:1, enabled:true, tags:[]}]);
  assert.deepEqual(normalizeJobs([]), []);
});
check('zero, false, empty tags and explicit undefined survive', () => {
  assert.deepEqual(normalizeJobs([{id:'a', count:0, enabled:false, tags:[]},
    {id:'b', count:undefined, enabled:undefined, tags:undefined}]), [
    {id:'a', count:0, enabled:false, tags:[]},
    {id:'b', count:1, enabled:true, tags:[]}]);
});
check('invalid roots, nonplain jobs, empty and duplicate ids', () => {
  for (const value of [null, undefined, {}, 'x', 0, [null], [[]], [new Date()],
    [{id:''}], [{id:'  '}], [{id:4}], [{id:'a'}, {id:' a '}],
    [Object.assign(Object.create({x:1}), {id:'a'})]]) {
    assert.throws(() => normalizeJobs(value), TypeError);
  }
});
check('strict count, boolean and tag validation', () => {
  for (const count of [null, -1, 0.5, NaN, Infinity, '0', false]) {
    assert.throws(() => normalizeJobs([{id:'a', count}]), TypeError);
  }
  for (const enabled of [null, 0, 1, 'false', []]) {
    assert.throws(() => normalizeJobs([{id:'a', enabled}]), TypeError);
  }
  for (const tags of [null, '', {}, [1], ['ok', false]]) {
    assert.throws(() => normalizeJobs([{id:'a', tags}]), TypeError);
  }
});
check('input immutability and bidirectional alias isolation', () => {
  const input = [{id:' a ', tags:['one']}];
  const first = normalizeJobs(input), second = normalizeJobs(input);
  assert.deepEqual(input, [{id:' a ', tags:['one']}]);
  assert.notEqual(first[0], input[0]);
  assert.notEqual(first[0].tags, input[0].tags);
  first[0].tags.push('two');
  input[0].tags.push('three');
  assert.deepEqual(second[0].tags, ['one']);
  assert.deepEqual(first[0].tags, ['one', 'two']);
  assert.deepEqual(input[0].tags, ['one', 'three']);
});
check('distinct default arrays and frozen input', () => {
  const input = Object.freeze([Object.freeze({id:'a', tags:Object.freeze(['x'])}),
                               Object.freeze({id:'b'})]);
  assert.deepEqual(normalizeJobs(input)[0].tags, ['x']);
  const output = normalizeJobs([{id:'a'}, {id:'b'}]);
  output[0].tags.push('x');
  assert.deepEqual(output[1].tags, []);
});
console.log(JSON.stringify({groups:results, passed:results.filter(x=>x.passed).length,
                            total:results.length}));
process.exitCode = results.every(x=>x.passed) ? 0 : 1;
