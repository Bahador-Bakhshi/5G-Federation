graph [
  node [
    id 0
    label 1
    disk 8
    cpu 2
    memory 3
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 4
    memory 13
  ]
  node [
    id 2
    label 3
    disk 8
    cpu 3
    memory 12
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 2
    memory 4
  ]
  node [
    id 4
    label 5
    disk 9
    cpu 2
    memory 4
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 4
    memory 8
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 25
    bw 58
  ]
  edge [
    source 0
    target 1
    delay 30
    bw 114
  ]
  edge [
    source 1
    target 2
    delay 30
    bw 150
  ]
  edge [
    source 2
    target 3
    delay 31
    bw 152
  ]
  edge [
    source 2
    target 4
    delay 25
    bw 138
  ]
  edge [
    source 2
    target 5
    delay 30
    bw 171
  ]
]
