graph [
  node [
    id 0
    label 1
    disk 8
    cpu 4
    memory 2
  ]
  node [
    id 1
    label 2
    disk 8
    cpu 3
    memory 1
  ]
  node [
    id 2
    label 3
    disk 4
    cpu 4
    memory 1
  ]
  node [
    id 3
    label 4
    disk 2
    cpu 1
    memory 3
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 1
    memory 13
  ]
  node [
    id 5
    label 6
    disk 10
    cpu 4
    memory 1
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 35
    bw 138
  ]
  edge [
    source 0
    target 1
    delay 35
    bw 58
  ]
  edge [
    source 0
    target 2
    delay 35
    bw 164
  ]
  edge [
    source 1
    target 5
    delay 32
    bw 143
  ]
  edge [
    source 2
    target 3
    delay 30
    bw 128
  ]
  edge [
    source 3
    target 4
    delay 25
    bw 98
  ]
]
