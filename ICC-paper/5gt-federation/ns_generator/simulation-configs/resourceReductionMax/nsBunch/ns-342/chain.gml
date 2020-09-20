graph [
  node [
    id 0
    label 1
    disk 9
    cpu 1
    memory 3
  ]
  node [
    id 1
    label 2
    disk 4
    cpu 1
    memory 6
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 2
    memory 5
  ]
  node [
    id 3
    label 4
    disk 6
    cpu 4
    memory 2
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 1
    memory 7
  ]
  node [
    id 5
    label 6
    disk 8
    cpu 3
    memory 6
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 25
    bw 171
  ]
  edge [
    source 0
    target 1
    delay 28
    bw 75
  ]
  edge [
    source 1
    target 2
    delay 30
    bw 131
  ]
  edge [
    source 1
    target 3
    delay 35
    bw 170
  ]
  edge [
    source 3
    target 4
    delay 33
    bw 139
  ]
  edge [
    source 4
    target 5
    delay 29
    bw 101
  ]
]
