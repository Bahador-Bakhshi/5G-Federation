graph [
  node [
    id 0
    label 1
    disk 10
    cpu 1
    memory 11
  ]
  node [
    id 1
    label 2
    disk 8
    cpu 1
    memory 14
  ]
  node [
    id 2
    label 3
    disk 7
    cpu 4
    memory 8
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 3
    memory 1
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 3
    memory 3
  ]
  node [
    id 5
    label 6
    disk 6
    cpu 2
    memory 11
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 28
    bw 100
  ]
  edge [
    source 0
    target 1
    delay 30
    bw 139
  ]
  edge [
    source 0
    target 2
    delay 28
    bw 86
  ]
  edge [
    source 1
    target 4
    delay 30
    bw 168
  ]
  edge [
    source 2
    target 3
    delay 33
    bw 171
  ]
  edge [
    source 3
    target 5
    delay 28
    bw 72
  ]
  edge [
    source 4
    target 5
    delay 31
    bw 161
  ]
]
