graph [
  node [
    id 0
    label 1
    disk 9
    cpu 2
    memory 10
  ]
  node [
    id 1
    label 2
    disk 9
    cpu 4
    memory 6
  ]
  node [
    id 2
    label 3
    disk 4
    cpu 4
    memory 12
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
    disk 7
    cpu 3
    memory 6
  ]
  node [
    id 5
    label 6
    disk 6
    cpu 4
    memory 9
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 28
    bw 115
  ]
  edge [
    source 0
    target 1
    delay 31
    bw 69
  ]
  edge [
    source 0
    target 2
    delay 26
    bw 177
  ]
  edge [
    source 0
    target 3
    delay 31
    bw 138
  ]
  edge [
    source 1
    target 4
    delay 32
    bw 141
  ]
  edge [
    source 2
    target 5
    delay 30
    bw 114
  ]
  edge [
    source 3
    target 5
    delay 26
    bw 50
  ]
  edge [
    source 4
    target 5
    delay 31
    bw 190
  ]
]
