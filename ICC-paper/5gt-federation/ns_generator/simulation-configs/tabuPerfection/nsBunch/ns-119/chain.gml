graph [
  node [
    id 0
    label 1
    disk 3
    cpu 2
    memory 12
  ]
  node [
    id 1
    label 2
    disk 9
    cpu 4
    memory 8
  ]
  node [
    id 2
    label 3
    disk 5
    cpu 4
    memory 12
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 2
    memory 14
  ]
  node [
    id 4
    label 5
    disk 3
    cpu 1
    memory 6
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 4
    memory 3
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 31
    bw 131
  ]
  edge [
    source 0
    target 1
    delay 30
    bw 67
  ]
  edge [
    source 0
    target 2
    delay 27
    bw 176
  ]
  edge [
    source 0
    target 3
    delay 26
    bw 105
  ]
  edge [
    source 1
    target 5
    delay 25
    bw 117
  ]
  edge [
    source 2
    target 4
    delay 32
    bw 197
  ]
  edge [
    source 3
    target 5
    delay 27
    bw 173
  ]
  edge [
    source 4
    target 5
    delay 27
    bw 139
  ]
]
