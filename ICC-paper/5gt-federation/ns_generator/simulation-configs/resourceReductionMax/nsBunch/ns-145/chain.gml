graph [
  node [
    id 0
    label 1
    disk 6
    cpu 4
    memory 4
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 2
    memory 15
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 3
    memory 16
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 4
    memory 1
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 3
    memory 11
  ]
  node [
    id 5
    label 6
    disk 8
    cpu 2
    memory 10
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 25
    bw 106
  ]
  edge [
    source 0
    target 1
    delay 35
    bw 117
  ]
  edge [
    source 1
    target 2
    delay 28
    bw 131
  ]
  edge [
    source 1
    target 3
    delay 33
    bw 182
  ]
  edge [
    source 1
    target 4
    delay 25
    bw 190
  ]
  edge [
    source 2
    target 5
    delay 31
    bw 194
  ]
  edge [
    source 3
    target 5
    delay 28
    bw 196
  ]
  edge [
    source 4
    target 5
    delay 35
    bw 112
  ]
]
