graph [
  node [
    id 0
    label 1
    disk 3
    cpu 2
    memory 10
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 3
    memory 3
  ]
  node [
    id 2
    label 3
    disk 5
    cpu 3
    memory 11
  ]
  node [
    id 3
    label 4
    disk 7
    cpu 3
    memory 12
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 3
    memory 16
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 2
    memory 14
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 164
  ]
  edge [
    source 0
    target 1
    delay 26
    bw 114
  ]
  edge [
    source 1
    target 2
    delay 30
    bw 179
  ]
  edge [
    source 2
    target 3
    delay 31
    bw 53
  ]
  edge [
    source 3
    target 4
    delay 35
    bw 104
  ]
  edge [
    source 3
    target 5
    delay 35
    bw 100
  ]
]
