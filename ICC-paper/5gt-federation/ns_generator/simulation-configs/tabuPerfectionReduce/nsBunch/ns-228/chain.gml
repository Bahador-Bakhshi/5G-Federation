graph [
  node [
    id 0
    label 1
    disk 1
    cpu 1
    memory 5
  ]
  node [
    id 1
    label 2
    disk 9
    cpu 1
    memory 3
  ]
  node [
    id 2
    label 3
    disk 4
    cpu 1
    memory 9
  ]
  node [
    id 3
    label 4
    disk 6
    cpu 3
    memory 11
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 1
    memory 15
  ]
  node [
    id 5
    label 6
    disk 9
    cpu 4
    memory 14
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 33
    bw 53
  ]
  edge [
    source 0
    target 1
    delay 31
    bw 67
  ]
  edge [
    source 0
    target 2
    delay 28
    bw 90
  ]
  edge [
    source 0
    target 3
    delay 32
    bw 101
  ]
  edge [
    source 1
    target 4
    delay 34
    bw 135
  ]
  edge [
    source 2
    target 5
    delay 31
    bw 178
  ]
  edge [
    source 3
    target 4
    delay 28
    bw 154
  ]
]
